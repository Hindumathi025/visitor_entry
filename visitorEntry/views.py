from django.shortcuts import render, redirect
from django.http import HttpResponse
import random

def visitor_entry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")

        # Generate OTP
        otp = random.randint(100000, 999999)
        request.session["otp"] = otp  # Store OTP in session
        request.session["mobile"] = mobile  # Store mobile number in session

        # Simulate sending OTP (Print in Console)
        print(f"OTP for {mobile} is {otp}")  # In production, use an SMS API

        return redirect("otp_verification")  # Redirect to OTP page

    return render(request, "index.html")

def otp_verification(request):
    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        mobile = request.session.get("mobile")
        correct_otp = request.session.get("otp")

        if correct_otp and int(entered_otp) == correct_otp:
            return render(request, "thank_you.html")
        else:
            return HttpResponse("Invalid OTP, please try again.")

    return render(request, "otp.html", {"mobile": request.session.get("mobile")})
