from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(max_length=191,label="Enter Your name")
    phone_number=forms.CharField(max_length=191,label="Enter Your phone number")