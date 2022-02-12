
from django.urls import path
from tution import views
urlpatterns = [

    path('', views.home_page,name="home"),
    
]
