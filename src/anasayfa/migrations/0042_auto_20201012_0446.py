# Generated by Django 3.1.1 on 2020-10-12 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0041_auto_20201012_0439'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MediaFile',
        ),
        migrations.AlterModelOptions(
            name='kuaslogomodel',
            options={'ordering': ['logo'], 'verbose_name': 'Şirket Logosu', 'verbose_name_plural': 'Şirket Logoları'},
        ),
    ]
