from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse


def home_page(request):
    if request.method=="POST":
        name=request.POST['name']
        
        
    return render(request,'home.html')
