from django.shortcuts import render

# Create your views here.

from .models import SoruModel,BaşlıkSoruModel
from anasayfa.views import  KuasLogoModel

def Soruview(request):
    objects = SoruModel.objects.all()
    maintitle = BaşlıkSoruModel.objects.last()
    logo =KuasLogoModel.objects.last()
    context = {
        'objects':objects,
        'maintitle':maintitle,
        'logo':logo
    }
    return render(request, "sorular.html", context)