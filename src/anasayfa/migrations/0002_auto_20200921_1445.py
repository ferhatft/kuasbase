# Generated by Django 3.1.1 on 2020-09-21 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='i̇nspectimage',
            options={'verbose_name': 'Resim', 'verbose_name_plural': 'Resimler'},
        ),
        migrations.AlterModelOptions(
            name='i̇nspectmodel',
            options={'ordering': ['title'], 'verbose_name': 'Giriş Açıklaması', 'verbose_name_plural': 'Giriş Açıklaması'},
        ),
    ]
