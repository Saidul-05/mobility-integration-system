from django.urls import path
from .views import ServiceListCreateView, ServiceDetailView
from .checkout import StripeCheckoutView

urlpatterns = [
    path("services/", ServiceListCreateView.as_view(), name="service-list"),
    path("services/<int:pk>/", ServiceDetailView.as_view(), name="service-detail"),
    path("checkout/", StripeCheckoutView.as_view(), name="stripe-checkout"),
]
