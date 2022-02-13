
from django.urls import path
from tution import views
urlpatterns = [

   # path('', views.home_page,name="home"),
    # path('', views.home_page,name="home"),
    path('contact/', views.ContactView.as_view(),name="contact"),
    path('post/', views.view_post,name="view_post"),
    path('postlist/', views.PostListView.as_view(),name="postlist"),
    # path('postcreate/', views.postcreate,name="postcreate"),
    path('postcreate/', views.PostCreateView.as_view(),name="postcreate"),
    path('subview/', views.subview,name="subview"),
    
]
