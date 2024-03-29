# Generated by Django 3.1.1 on 2021-05-03 15:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_delete_blognasayfamodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='author',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Yazar'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='main_context',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Giriş Paragrafı  '),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='main_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Ana Fotoğraf '),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(blank=True, max_length=500, verbose_name='Başlık'),
        ),
    ]
