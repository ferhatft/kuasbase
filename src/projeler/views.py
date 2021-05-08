from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse

from .models import *


from anasayfa.views import  KuasLogoModel

def projeview(request):
    galerimodel = GaleriModel.objects.all()
    maintitle = GaleriAnasayfaModel.objects.last()
    
    logo =KuasLogoModel.objects.last()

    context = {
        'galerimodel': galerimodel,
        'maintitle':maintitle,
        'logo':logo
    }

    return render(request, "galeri.html", context)




def projedetailview(request, pk):
    instance = get_object_or_404(GaleriModel, pk=pk)
    image_list = instance.images.all()


    logo =KuasLogoModel.objects.last()

    context = {
        'object': instance,
        'image_list':image_list,
        'logo':logo
    }

    return render(request, "galeri_detail.html", context)

