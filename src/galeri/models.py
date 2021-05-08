
import os
import uuid
from django.dispatch import receiver
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class GaleriModel(models.Model):
    main_image              = models.FileField(blank=True ,null=True, verbose_name="Ana fotoğraf '1920x900'")
    title                   = models.CharField(max_length=500,verbose_name = "Başlık ")
    subtitle                = models.CharField(max_length=500,verbose_name = "Alt başlık",null=True,blank=True)
    content                 = RichTextUploadingField(blank=True, null=True, verbose_name="ek metin  ")
    imageone                = models.ImageField(verbose_name = "Ana Resim bir", blank=True, null=True )
    imagetwo                = models.ImageField(verbose_name = "Ana Resim iki", blank=True, null=True)
    imagetree               = models.ImageField(verbose_name = "Ana Resim üç", blank=True, null=True)
    imagefour               = models.ImageField(verbose_name = "Ana Resim dört", blank=True, null=True)




    def __str__(self):
        return '%s %s' % (self.title, self.id)

    
    def get_absolute_url(self):
        return "/galeri/{pk}/".format(pk=self.pk)

    class Meta:
        ordering = ['title']
        verbose_name = 'Galeri Ürün'
        verbose_name_plural = 'Galeri Ürünler'



# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=GaleriModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `sender` object is deleted.
    """
    if instance.main_image:
        if os.path.isfile(instance.main_image.path):
            os.remove(instance.main_image.path)

    if instance.imageone:
        if os.path.isfile(instance.imageone.path):
            os.remove(instance.imageone.path)

    if instance.imagetwo:
        if os.path.isfile(instance.imagetwo.path):
            os.remove(instance.imagetwo.path)

    if instance.imagetree:
        if os.path.isfile(instance.imagetree.path):
            os.remove(instance.imagetree.path)

    if instance.imagefour:
        if os.path.isfile(instance.imagefour.path):
            os.remove(instance.imagefour.path)


@receiver(models.signals.pre_save, sender=GaleriModel)
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

#
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).imageone
    except sender.DoesNotExist:
        return False

    new_file = instance.imageone
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

#
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).imagetwo
    except sender.DoesNotExist:
        return False

    new_file = instance.imagetwo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

#

    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).imagetree
    except sender.DoesNotExist:
        return False

    new_file = instance.imagetree
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

#

    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).imagefour
    except sender.DoesNotExist:
        return False

    new_file = instance.imagefour
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


    


class GaleriImage(models.Model):
    galerimodel             = models.ForeignKey(GaleriModel, related_name='images', on_delete=models.CASCADE) 
    image                   = models.ImageField()

    class Meta:
        verbose_name = 'Detay Resim'
        verbose_name_plural = 'Detay Resim'

# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=GaleriImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `sender` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=GaleriImage)
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




class GaleriAnasayfaModel(models.Model):
    pagetitle =models.CharField(max_length=500,verbose_name = "Anasayfa başlık ",null=True,blank=True)
    pagesubtitle =models.CharField(max_length=500,verbose_name = "altbaşlık ",null=True,blank=True)
    main_image = models.FileField(blank=True ,null=True, verbose_name="fotoğraf '1920x900'")
   
    
    def __str__(self):
        return '%s' % (self.pagetitle)

    class Meta:
        ordering = ['id']
        verbose_name = 'Galeri ana sayfa'
        verbose_name_plural = 'Galeri ana sayfa'


# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=GaleriAnasayfaModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `sender` object is deleted.
    """
    if instance.main_image:
        if os.path.isfile(instance.main_image.path):
            os.remove(instance.main_image.path)

@receiver(models.signals.pre_save, sender=GaleriAnasayfaModel)
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

