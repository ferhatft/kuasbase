# Generated by Django 3.1.1 on 2020-09-24 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0013_auto_20200924_0440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='i̇nspectmodel',
            name='paragrafbir',
        ),
        migrations.RemoveField(
            model_name='i̇nspectmodel',
            name='paragrafdört',
        ),
        migrations.RemoveField(
            model_name='i̇nspectmodel',
            name='paragrafiki',
        ),
        migrations.RemoveField(
            model_name='i̇nspectmodel',
            name='paragrafüç',
        ),
        migrations.RemoveField(
            model_name='i̇nspectmodel',
            name='titleiki',
        ),
        migrations.AddField(
            model_name='i̇nspectmodel',
            name='Subtitle',
            field=models.CharField(blank=True, max_length=500, verbose_name='Altbaşlık Ekleyin'),
        ),
        migrations.AddField(
            model_name='i̇nspectmodel',
            name='main_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Ana Fotoğrafı Ekleyin'),
        ),
        migrations.AlterField(
            model_name='i̇nspectmodel',
            name='title',
            field=models.CharField(blank=True, max_length=500, verbose_name='Başlık Ekleyin'),
        ),
    ]
