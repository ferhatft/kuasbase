# Generated by Django 3.1.1 on 2020-10-12 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0035_auto_20201012_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kuaslogomodeliki',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Şirket Logosu Ekleyin '),
        ),
        migrations.AlterField(
            model_name='kuaslogomodeliki',
            name='minlogo',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Şirket Küçük Logo Ekleyin '),
        ),
    ]
