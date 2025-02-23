import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Service

class StripeCheckoutView(APIView):
    """
    POST /api/checkout/
    Expects JSON: { 'service_id': <ID> }
    Returns: { 'sessionId': <stripe_session_id> }
    """

    def post(self, request):
        service_id = request.data.get('service_id')
        if not service_id:
            return Response({"error": "No service_id provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            service = Service.objects.get(id=service_id)
        except Service.DoesNotExist:
            return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)

        # Load Stripe key from settings or .env
        stripe.api_key = getattr(settings, "STRIPE_SECRET_KEY", None)
        if not stripe.api_key:
            return Response({"error": "Stripe secret key not configured"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Create Stripe Checkout Session
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[{
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": service.name},
                        "unit_amount": int(service.price * 100),  # convert dollars to cents
                    },
                    "quantity": 1,
                }],
                mode="payment",
                success_url="http://localhost:3000/success",  # or your production URL
                cancel_url="http://localhost:3000/cancel",
            )
            return Response({"sessionId": session.id}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
