from django.conf.urls import url

from django.urls import path

from .views import (
    galeriview,
    galeridetailview,
)


app_name = 'galeri'

urlpatterns = [
    path('' , galeriview, name="galeri"),
    path('<int:pk>/', galeridetailview, name= "galeri_detail"),
]



   
  