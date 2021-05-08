# Generated by Django 3.1.1 on 2021-05-05 12:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorular', '0009_auto_20210504_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='başlıksorumodel',
            name='main_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name="Fotoğraf '1920x900 '"),
        ),
        migrations.AlterField(
            model_name='başlıksorumodel',
            name='maincontent',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=500, null=True, verbose_name='açıklama '),
        ),
    ]
