
from django.contrib import admin
from django.urls import path,include
from .views import HomeView
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(template_name='home.html'),name="homeview"),
    path('tution/', include('tution.urls')),
    path('session/', include('session.urls')),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
