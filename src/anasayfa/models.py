
import os
import uuid
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete

from ckeditor.fields import RichTextField

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class KuasLogoModel(models.Model):
   
    logo = models.FileField(verbose_name="Şirket Logosu Ekleyin ")
    minlogo = models.FileField(verbose_name="Şirket Küçük Logo Ekleyin ", null=True)
    
    
    def __str__(self):
        return '%s %s' % (self.logo, 'Logo')

    class Meta:
        ordering = ['logo']
        verbose_name = 'Kuas logo'
        verbose_name_plural = 'Kuas logo'


# Delete exist logo

# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=KuasLogoModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `sender` object is deleted.
    """
    if instance.logo:
        if os.path.isfile(instance.logo.path):
            os.remove(instance.logo.path)

    if instance.minlogo:
        if os.path.isfile(instance.minlogo.path):
            os.remove(instance.minlogo.path)

# @receiver(models.signals.pre_save, sender=KuasLogoModel)
# def auto_delete_file_on_change(sender, instance, **kwargs):

@receiver(models.signals.pre_save, sender=KuasLogoModel)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `sender` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = KuasLogoModel.objects.get(pk=instance.pk).logo
    except KuasLogoModel.DoesNotExist:
        return False

    new_file = instance.logo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
#

    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).minlogo
    except sender.DoesNotExist:
        return False

    new_file = instance.minlogo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)




class İnspectModel(models.Model):
    title = models.CharField(max_length=500,verbose_name = "Başlık '1' ", blank=True)
    contextmain = models.TextField(max_length=500,verbose_name = "açıklama '2' ", blank=True,null=True)
    formtitle = models.CharField(max_length=500,verbose_name = "form başlık  '3' ", blank=True)
    formcontext = models.TextField(max_length=500,verbose_name = "form açıklama '4' ", blank=True)
    main_image = models.FileField(blank=True , null=True, verbose_name="Arka plan ")
    richtext                   = RichTextUploadingField(blank=True, null=True, verbose_name="ek metin '5' ")
    
    
    def __str__(self):
        return '%s %s' % ('1 - 6', 'Giriş ')

    class Meta:
        ordering = ['id']
        verbose_name = '1- Bölüm bir '
        verbose_name_plural = '1- Bölüm bir'


# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=İnspectModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `sender` object is deleted.
    """
    if instance.main_image:
        if os.path.isfile(instance.main_image.path):
            os.remove(instance.main_image.path)

@receiver(models.signals.pre_save, sender=İnspectModel)
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



class İnspectImage(models.Model):
    inspectmodel = models.ForeignKey(İnspectModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

    class Meta:
        verbose_name = 'Resim'
        verbose_name_plural = "Resimler '6' "



# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=İnspectImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `sender` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=İnspectImage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `sender` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)





class ReferansModel(models.Model):
    title = models.CharField(max_length=500,verbose_name = "Başlık '7'", blank=True)
    # paragrafbir = models.CharField(max_length=500,verbose_name = "Açıklama '8' " ,blank=True )
    
    richtext                   = RichTextUploadingField(blank=True, null=True, verbose_name="ek metin '8' ")
   
    
    def __str__(self):
        return '%s %s' % ('7-10', 'Bölüm iki')

    class Meta:
        ordering = ['id']
        verbose_name = '2- Bölüm iki'
        verbose_name_plural = '2- Bölüm iki'


class ReferansImage(models.Model):
    referansmodel = models.ForeignKey(ReferansModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

    class Meta:
        verbose_name = 'Resim'
        verbose_name_plural = "Resimler '9'"



# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=ReferansImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `sender` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=ReferansImage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `sender` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).image
    except sender.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class WhoweareModel(models.Model):
    title = models.CharField(max_length=500,verbose_name = "Başlık '10' ", blank=True)
    main_image = models.FileField(blank=True , null=True, verbose_name="Fotoğraf '11' ")
    subtitle = models.CharField(max_length=500,verbose_name = "Alt başlık '12' ", blank=True)
    sub_image = models.FileField(blank=True , null=True, verbose_name="Fotoğrafı '13'")
    richtext                   = RichTextUploadingField(blank=True, null=True, verbose_name="ek metin '14' ")
    
    def __str__(self):
        return '%s %s' % ('10-14', 'Bölüm üç')

    class Meta:
        ordering = ['id']
        verbose_name = '3- Bölüm üç'
        verbose_name_plural = '3- Bölüm üç '



# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=WhoweareModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `sender` object is deleted.
    """
    if instance.main_image:
        if os.path.isfile(instance.main_image.path):
            os.remove(instance.main_image.path)
    
    # subimage 

    if instance.sub_image:
        if os.path.isfile(instance.sub_image.path):
            os.remove(instance.sub_image.path)

@receiver(models.signals.pre_save, sender=WhoweareModel)
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

    
    # subimage

    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).sub_image
    except sender.DoesNotExist:
        return False

    new_file = instance.sub_image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

    
   

class WhatwedoModel(models.Model):
    title = models.CharField(max_length=500,verbose_name = "Başlık '15'", blank=True)
    main_image = models.FileField(blank=True , null=True, verbose_name="Fotoğraf '16'")
    subtitle = models.CharField(max_length=500,verbose_name = "Altbaşlık '17'", blank=True)
    richtext                   = RichTextUploadingField(blank=True, null=True, verbose_name="ek metin '18' ")
    video = models.CharField(max_length=500,verbose_name = "Video iframe linki '19' ", blank=True)    
  
    def __str__(self):
        return '%s %s' % ('13-19', 'Bölüm dört')

    class Meta:
        ordering = ['id']
        verbose_name = '4- Bölüm dört'
        verbose_name_plural = '4- Bölüm dört'
   



# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=WhatwedoModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `sender` object is deleted.
    """
    if instance.main_image:
        if os.path.isfile(instance.immain_imageage.path):
            os.remove(instance.main_image.path)

@receiver(models.signals.pre_save, sender=WhatwedoModel)
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


