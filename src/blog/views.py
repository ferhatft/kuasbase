from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from partial_date import PartialDate
from .models import  *

from anasayfa.views import  KuasLogoModel

# Create your views here.


def BlogView(request):
    blogmdel = BlogModel.objects.all()
    logo =KuasLogoModel.objects.last()

    context = {
        'blogmdel': blogmdel,
        'logo':logo,
    }

    return render(request, "blog.html", context)




def BlogDetailView(request,pk):
    blogmdel = get_object_or_404(BlogModel, pk=pk)

    image_list = blogmdel.images.all()

    logo =KuasLogoModel.objects.last()


    context = {
        'blogmdel': blogmdel,
        'image_list':image_list,
        'logo':logo,
    }

    return render(request, "blog_detail.html", context)

