# Generated by Django 3.1.1 on 2021-05-03 15:58

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20210503_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogonlycontxt',
            name='inspectmodel',
        ),
        migrations.RemoveField(
            model_name='blogmodel',
            name='author',
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='main_context',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='main_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf '),
        ),
        migrations.DeleteModel(
            name='BlogImage',
        ),
        migrations.DeleteModel(
            name='BlogonlyContxt',
        ),
    ]
