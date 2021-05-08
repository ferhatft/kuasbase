"""kuasbase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
# from django.conf.urls import include
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import *

from anasayfa.views import *

from galeri.views import *

from sorular.views import Soruview

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^admin/', admin.site.urls),

    path('', home_page, name="home"),
    
    path('sikca_sorulan_sorular/', Soruview, name="sorular"),
    # url(r'^$', home_page, name='home'),
    # url(r'^sikca_sorulan_sorular/$', Soruview, name='sorular'),

    path('galeri/', include("galeri.urls")),
    
    path('projeler/', include("projeler.urls")),
    path('blog/', include("blog.urls")),
    path('iletisim/', include("iletisim.urls")),
    # url(r'^galeri/', include("galeri.urls")),
    # url(r'^blog/', include("blog.urls")),
    # url(r'^iletisim/', include("iletisim.urls")),
    # url(r'^referanslar', include("referanslar.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
   
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,
                                       document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,
                                       document_root=settings.MEDIA_ROOT)

#     url(r'^$', home_page, name='home'),
#     url(r'^about/$', about_page, name='about'),
#     url(r'^contact/$', contact_page, name='contact'),
#     url(r'^login/$', LoginView.as_view(), name='login'),
#     url(r'^checkout/address/create/$', checkout_address_create_view, name='checkout_address_create'),
#     url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name='checkout_address_reuse'),
#     url(r'^register/guest/$', guest_register_view, name='guest_register'),
#     url(r'^logout/$', LogoutView.as_view(), name='logout'),
#     url(r'^api/cart/$', cart_detail_api_view, name='api-cart'),
#     url(r'^cart/', include("carts.urls", namespace='cart')),
#     url(r'^billing/payment-method/$', payment_method_view, name='billing-payment-method'),
#     url(r'^billing/payment-method/create/$', payment_method_createview, name='billing-payment-method-endpoint'),
#     url(r'^register/$', RegisterView.as_view(), name='register'),
#     url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html')),
#     url(r'^products/', include("products.urls", namespace='products')),
#     url(r'^search/', include("search.urls", namespace='search')),
#     url(r'^admin/', admin.site.urls),
