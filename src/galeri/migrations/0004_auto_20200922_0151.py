# Generated by Django 3.1.1 on 2020-09-21 22:51

from django.db import migrations, models
import galeri.models


class Migration(migrations.Migration):

    dependencies = [
        ('galeri', '0003_auto_20200922_0051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galerimodel',
            options={'ordering': ['title'], 'verbose_name': 'Ürün Açıklaması', 'verbose_name_plural': 'Ürün Açıklamaları'},
        ),
        migrations.AlterField(
            model_name='galerimodel',
            name='imagefour',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Ana Resim dört'),
        ),
        migrations.AlterField(
            model_name='galerimodel',
            name='imageone',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Ana Resim bir'),
        ),
        migrations.AlterField(
            model_name='galerimodel',
            name='imagetree',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Ana Resim üç'),
        ),
        migrations.AlterField(
            model_name='galerimodel',
            name='imagetwo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Ana Resim iki'),
        ),
        migrations.CreateModel(
            name='GaleriImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('galerimodel', models.ForeignKey(on_delete=galeri.models.GaleriModel, related_name='images', to='galeri.galerimodel')),
            ],
            options={
                'verbose_name': 'Detay Sayfası Resimi',
                'verbose_name_plural': 'Detay Sayfası Resimleri',
            },
        ),
    ]