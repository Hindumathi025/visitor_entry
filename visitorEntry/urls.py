from django.urls import path
from .views import visitor_entry, otp_verification

urlpatterns = [
    path('', visitor_entry, name="visitor_entry"),  # Show form first
    path('otp/', otp_verification, name="otp_verification"),  # OTP page
]
