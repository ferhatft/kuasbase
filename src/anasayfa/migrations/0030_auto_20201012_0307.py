# Generated by Django 3.1.1 on 2020-10-12 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0029_mediafile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Arka plan fotoğrafı ekleyin'),
        ),
    ]
