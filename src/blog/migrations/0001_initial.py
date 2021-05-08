# Generated by Django 3.1.1 on 2020-09-23 16:10

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='Başlık bir')),
                ('paragrafbir', models.CharField(blank=True, max_length=500, verbose_name='Açıklama bir')),
                ('paragrafiki', models.CharField(blank=True, max_length=500, verbose_name='Açıklama iki')),
                ('titleiki', models.CharField(blank=True, max_length=500, verbose_name='Başlık iki')),
                ('paragrafüç', models.CharField(blank=True, max_length=500, verbose_name='Açıklama üç')),
                ('paragrafdört', models.CharField(max_length=500, verbose_name='Açıklama dört')),
            ],
            options={
                'verbose_name': 'Giriş Açıklaması',
                'verbose_name_plural': 'Giriş Açıklaması',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('context', models.CharField(max_length=500, verbose_name='resim açıklaması')),
                ('inspectmodel', models.ForeignKey(on_delete=blog.models.BlogModel, related_name='images', to='blog.blogmodel')),
            ],
            options={
                'verbose_name': 'Resim+içerik',
                'verbose_name_plural': 'Resim+içerik',
            },
        ),
    ]
