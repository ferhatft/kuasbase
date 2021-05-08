from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse

from .models import İnspectModel,İnspectImage,ReferansModel,ReferansImage,WhoweareModel,WhatwedoModel,KuasLogoModel


from django.core.mail import send_mail
from iletisim.forms import  ContactForm
# Create your views here.

def home_page(request):
    obj = İnspectModel.objects.last()

    try:
        image_list = obj.images.all()
    except:
        image_list = None

    referanslar = ReferansModel.objects.last()

    try:
        referans_image_list =  referanslar.images.all()
    except:
        referans_image_list = None

    whowearemodel = WhoweareModel.objects.last()
    whatwedomodel = WhatwedoModel.objects.last()
    
    logo =KuasLogoModel.objects.last()


    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']
            # phone = form.cleaned_data['phone']
            
            send_mail (
                subject, # subject
                'Gönderen = ' + email + '\n' + message , #message
                'kuastinyhouse@gmail.com', #from email
                ['kuastinyhouse@gmail.com'], # To email    
            )

            send_mail (
                'Kuas Tiny Hause ', # subject
                'İletişime geçtiğiniz için teşekkür ederiz en kısa sürede size dönüş yapılacaktır', #message
                'kuastinyhouse@gmail.com', #from email
                [email], # To email    
            )

            form.save()
            # messages.success(
            # request, 'Mesajınız başarıyla gönderildi. En kısa sürede size dönüş yapılcaktır...')
            return redirect('home')
    else:
        form = ContactForm()
 
    context = {
        'obj':obj,
        'image_list':image_list,
        'referanslar':referanslar,
        'referans_image_list':referans_image_list,
        'whowearemodel':whowearemodel,
        'whatwedomodel':whatwedomodel,
        'logo':logo,
        'form':form,
    }
    return render(request, "index.html", context)
