from django.conf.urls import url

from django.urls import path

from .views import (
    projeview,
    projedetailview,
    # checkout_home,
    # checkout_done_view,
)


app_name = 'projeler'

urlpatterns = [
    path('' , projeview, name="proje"),
    path('<int:pk>/', projedetailview, name= "proje_detail"),
]



   
  