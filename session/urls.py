
from django.urls import path
from session import views
app_name='session'
urlpatterns = [

     path('userlogin/', views.userlogin, name="usersession"),
     path('logout/', views.userlogout, name="userlogout"),
     path('registration/', views.registration, name="signup"),
     path('changepassword/', views.changepassword, name="changepassword"),
    
]
