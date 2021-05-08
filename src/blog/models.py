
import os
import uuid
from django.dispatch import receiver
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class BlogModel(models.Model):
    title                   = models.CharField(max_length=500,verbose_name = "Başlık", blank=True)
    # author                  = models.CharField(max_length=500,verbose_name = "Yazar",blank=True, null=True)
    created_date            = models.DateTimeField(auto_now_add=True,null=True,verbose_name="Oluşturulma Tarihi")
    main_image              = models.FileField(blank=True ,null=True, verbose_name="Fotoğraf '1920x900' ")
    main_context            = RichTextUploadingField( verbose_name = "İçerik" , blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.title, self.id)

        
    def get_absolute_url(self):
        return "/blog/{pk}/".format(pk=self.pk)

    class Meta:
        ordering = ['title']
        verbose_name = 'Blog yazısı'
        verbose_name_plural = 'Blog yazıları'


# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=BlogModel)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `sender` object is deleted.
    """
    if instance.main_image:
        if os.path.isfile(instance.main_image.path):
            os.remove(instance.main_image.path)

@receiver(models.signals.pre_save, sender=BlogModel)
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



class BlogonlyImage(models.Model):
    inspectmodel = models.ForeignKey(BlogModel, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

    class Meta:
        verbose_name = 'Blog resim galerisi'
        verbose_name_plural = 'Blog resim galerisi'



# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=BlogonlyImage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `sender` object is deleted.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=BlogonlyImage)
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



