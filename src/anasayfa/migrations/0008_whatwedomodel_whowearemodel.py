# Generated by Django 3.1.1 on 2020-09-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0007_referansimage_referansmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatwedoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='Başlık Ekleyin')),
                ('subtitle', models.CharField(blank=True, max_length=500, verbose_name='Altbaşlık Ekleyin')),
                ('paragrafbir', models.CharField(blank=True, max_length=500, verbose_name='Açıklama Ekleyin')),
                ('paragrafiki', models.CharField(blank=True, max_length=500, verbose_name='Açıklama Ekleyin')),
                ('paragrafüç', models.CharField(blank=True, max_length=500, verbose_name='Açıklama Ekleyin')),
            ],
            options={
                'verbose_name': 'Biz ne yapıyoruz',
                'verbose_name_plural': 'Biz ne yapıyoruz',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='WhoweareModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='Başlık Ekleyin')),
                ('subtitle', models.CharField(blank=True, max_length=500, verbose_name='Altbaşlık Ekleyin')),
                ('paragrafbir', models.CharField(blank=True, max_length=500, verbose_name='Açıklama Ekleyin')),
                ('paragrafiki', models.CharField(blank=True, max_length=500, verbose_name='Açıklama Ekleyin')),
                ('paragrafüç', models.CharField(blank=True, max_length=500, verbose_name='Açıklama Ekleyin')),
            ],
            options={
                'verbose_name': 'Biz Kimiz',
                'verbose_name_plural': 'Biz Kimiz',
                'ordering': ['title'],
            },
        ),
    ]
