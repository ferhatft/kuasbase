
import os
import uuid
from django.dispatch import receiver

from django.utils.translation import gettext_lazy as _
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

STATUS = (
    ('new', 'New'),
    ('read', 'Read'),
    ('closed', 'Closed'),
)


class Contact(models.Model):
    subject = models.CharField(max_length=25, null=True)
    status = models.CharField(max_length=6, choices=STATUS, default='new')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'


class İnfo(models.Model):
    street = models.CharField(null=True,max_length=300, verbose_name="Sokak")
    city = models.CharField(null=True,max_length=300, verbose_name="Şehir")
    postcode = models.CharField(null=True,max_length=300, verbose_name="Posta Kodu")
    detay = models.CharField(blank=True ,null=True,max_length=300, verbose_name="Varsa ekstra detaylar")
    email = models.CharField(max_length=300, verbose_name="Email Adresi")
    phone = models.CharField(max_length=300, verbose_name="Telefon Numarası")
    main_image = models.FileField(blank=True ,null=True, verbose_name="Ana Fotoğraf Ekleyin")
    title = models.CharField(max_length=500,verbose_name = "Ana Başlık ", blank=True)
    subtitle = models.CharField(max_length=500,verbose_name = "Alt Başlık ", blank=True,null=True )
    main_context            = RichTextField( verbose_name = "Ana Açıklama Ekleyin" , blank=True, null=True)
    campanydescrp         = RichTextField( verbose_name = "Şirket Açıklaması " , blank=True, null=True)


    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']
        verbose_name = 'Kuas  Bilgi'
        verbose_name_plural = 'Kuas  Bilgi'



# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=İnfo)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `sender` object is deleted.
    """
    if instance.main_image:
        if os.path.isfile(instance.main_image.path):
            os.remove(instance.main_image.path)

@receiver(models.signals.pre_save, sender=İnfo)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `sender` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).main_image
    except sender.DoesNotExist:
        return False

    new_file = instance.main_image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
