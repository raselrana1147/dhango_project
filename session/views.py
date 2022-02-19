from dataclasses import dataclass
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.mail import send_mail



# Create your views here.
def userlogin(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Successfully login")
                return redirect('homeview')
               
            else:
                messages.error(request,"Invalid username or Password")
        else:
             messages.error(request,"Invalid username or Password")
    else:
        form=AuthenticationForm()
    return render(request, 'login.html',{'form':form})

def userlogout(request):
    logout(request)
    messages.success(request,"Logout successfully")
    return redirect("homeview")

def registration(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            # current_site=get_current_site(request)
            # mail_subject="An Account creation"
            # message=render_to_string('email.html',{
            #         'user':user,
            #         'domain':current_site.domain
            #     })
            # send_mail=form.cleaned_data.get('email')
            # email=EmailMessage(mail_subject,message,to=[send_mail])
            # email.send()

            send_mail(
                'Subject here',
                'Here is the message.',
                'developer1000486@gmail.com',
                ['raselrana1147@gmail.com'],
                fail_silently=False,
            )

            messages.success(request,"Registration has been successfull")
            return redirect("session:usersession")
    else:
        form=SignUpForm
    return render(request,"registration.html",{"form":form})

def changepassword(request):
    if request.method=="POST":
        form=PasswordChangeForm(data=request.POST, user=request.user);
        if form.is_valid():
            update_session_auth_hash(request,form.user)
            messages.success(request,"Password change successfully")
            return redirect('homeview')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'password_chage.html',{"form":form})
            
    
    
