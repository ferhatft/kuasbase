# Generated by Django 3.1.1 on 2020-09-24 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0015_auto_20200924_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatwedomodel',
            name='main_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Ana Fotoğrafı Ekleyin'),
        ),
        migrations.AddField(
            model_name='whowearemodel',
            name='main_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Ana Fotoğrafı Ekleyin'),
        ),
    ]
