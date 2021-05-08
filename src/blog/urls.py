from django.conf.urls import url

from django.urls import path

from .views import (
    BlogView, 
    BlogDetailView,
)

app_name = 'blog'

urlpatterns = [
    path('' ,BlogView, name="blog"),
    path('<int:pk>/', BlogDetailView, name= "blog_detail"),
]

   
  