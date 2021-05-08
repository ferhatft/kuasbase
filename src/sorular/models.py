import os
import uuid
from django.dispatch import receiver
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.



class SoruModel(models.Model):
    soru = models.CharField(max_length=500,verbose_name = "Soru ")
    cevap             = RichTextField(verbose_name = "Cevap " , blank=True, null=True)
   
    
    def __str__(self):
        return '%s %s' % (self.soru, self.id)


    class Meta:
        ordering = ['id']
        verbose_name = 'Soru'
        verbose_name_plural = 'Sorular'



class BaşlıkSoruModel(models.Model):
    pagetitle               = models.CharField(max_length=500,verbose_name = "ana başlık ",null=True)
    pagesubtitle            = models.CharField(max_length=500,verbose_name = "alt başlık ",null=True ,blank=True)
    maincontent             = RichTextUploadingField(max_length=500,verbose_name = "açıklama ",null=True ,blank=True)
    main_image              = models.FileField(blank=True ,null=True, verbose_name="Fotoğraf '1920x900 '")
   
    
    def __str__(self):
        return '%s %s' % (self.pagetitle, self.id)

    class Meta:
        ordering = ['id']
        verbose_name = 'Sorular ana sayfa '
        verbose_name_plural = 'Sorular ana sayfa'




# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=BaşlıkSoruModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `sender` object is deleted.
    """
    if instance.main_image:
        if os.path.isfile(instance.main_image.path):
            os.remove(instance.main_image.path)

@receiver(models.signals.pre_save, sender=BaşlıkSoruModel)
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

