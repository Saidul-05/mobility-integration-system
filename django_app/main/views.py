import stripe
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from .models import Service
from .serializers import ServiceSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY if hasattr(settings, 'STRIPE_SECRET_KEY') else 'sk_test_xxx'

class ServiceListCreateView(...):
    # same as before

class ServiceDetailView(...):
    # same as before

class StripeCheckoutView(APIView):
    def post(self, request):
        service_id = request.data.get('service_id')
        service = Service.objects.get(id=service_id)
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': service.name},
                    'unit_amount': int(service.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://your-frontend-domain/success',
            cancel_url='http://your-frontend-domain/cancel',
        )
        return Response({'sessionId': session.id})
