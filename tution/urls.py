
from django.urls import path
from tution import views
app_name='tution'
urlpatterns = [

   # path('', views.home_page,name="home"),
    # path('', views.home_page,name="home"),
    # path('contact/', views.ContactView.as_view(),name="contact"),
     path('contact/', views.contact,name="contact"),
    path('post/', views.view_post,name="view_post"),
    path('postlist/', views.PostListView.as_view(),name="postlist"),
    # path('postcreate/', views.postcreate,name="postcreate"),
    path('postcreate/', views.PostCreateView.as_view(),name="postcreate"),
    path('postdetail/<int:pk>/', views.PostDetailView.as_view(),name="postdetail"),
    path('edit/<int:pk>/', views.PostEditView.as_view(),name="postedit"),
    path('delete/<int:pk>/', views.postDeleteView.as_view(),name="delete"),
    path('subview/', views.subview,name="subview"),
    path('search/', views.searchitem,name="searchitem"),
]
