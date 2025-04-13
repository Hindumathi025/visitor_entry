from django.urls import path
from . import views

urlpatterns = [
    path('',views.visitor_entry, name="visitor_entry"),  # Show form first
    path('verify-phone-email/', views.verify_phone_email, name="verify-phone-email"),  # OTP page
]
