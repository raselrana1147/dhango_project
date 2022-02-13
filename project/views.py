from http.client import HTTPResponse
from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView

def home(request):   
    return render(request,'home.html')

class HomeView(TemplateView):
    template_name='home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg']="Welcome toour website"
        return context
    
    