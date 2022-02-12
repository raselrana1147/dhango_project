from django.shortcuts import render

from django.shortcuts import render,HttpResponse
from .models import Contact
from .forms import ContactForm


def home_page(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            phone=form.cleaned_data['phone_number']
            contact=Contact(name=name,phone=phone);
            contact.save();
    else:
        form=ContactForm()
        
    return render(request,'home.html',{'form':form})

