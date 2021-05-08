from django.shortcuts import render,redirect

from .models import Contact, İnfo 
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.
from anasayfa.views import  KuasLogoModel



def contacview(request):
    obj = İnfo.objects.last()

    logo =KuasLogoModel.objects.last()
  

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name        = form.cleaned_data['name']
            email       = form.cleaned_data['email']
            message     = form.cleaned_data['message']
            subject     = form.cleaned_data['subject']
            send_mail (
                subject, # subject
                'Gönderen = ' + email + '\n' + message , #message
                'kuastinyhouse@gmail.com', #from email
                ['kuastinyhouse@gmail.com',], # To email    
            )

            send_mail (
               'Kuas Tiny Hause ', # subject
                'İletişime geçtiğiniz için teşekkür ederiz en kısa sürede size dönüş yapılacaktır', #message
                'kuastinyhouse@gmail.com', #from email
                [email], # To email    
            )

            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'obj': obj,
        'form': form,
        'logo':logo
    }
    return render(request, "contac.html", context)
