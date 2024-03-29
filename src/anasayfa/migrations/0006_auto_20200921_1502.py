# Generated by Django 3.1.1 on 2020-09-21 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0005_i̇nspectmodel_titleüç'),
    ]

    operations = [
        migrations.RenameField(
            model_name='i̇nspectmodel',
            old_name='paragraf',
            new_name='paragrafdört',
        ),
        migrations.RemoveField(
            model_name='i̇nspectmodel',
            name='titleüç',
        ),
        migrations.AddField(
            model_name='i̇nspectmodel',
            name='paragrafbir',
            field=models.CharField(blank=True, max_length=500, verbose_name='Açıklama bir'),
        ),
        migrations.AddField(
            model_name='i̇nspectmodel',
            name='paragrafiki',
            field=models.CharField(blank=True, max_length=500, verbose_name='Açıklama iki'),
        ),
        migrations.AddField(
            model_name='i̇nspectmodel',
            name='paragrafüç',
            field=models.CharField(blank=True, max_length=500, verbose_name='Açıklama üç'),
        ),
    ]
