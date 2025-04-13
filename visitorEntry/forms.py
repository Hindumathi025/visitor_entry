from django import forms

class VisitorForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    mobile = forms.CharField(max_length=10, required=True)

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, required=True)
