from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
	  class Meta:
	  	model=Contact
	  	fields='__all__'
    # name=forms.CharField(max_length=191,label="Enter Your name")
    # phone_number=forms.CharField(max_length=191,label="Enter Your phone number")