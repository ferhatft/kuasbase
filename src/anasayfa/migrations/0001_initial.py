# Generated by Django 3.1.1 on 2020-09-21 11:40

import anasayfa.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='İnspectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, verbose_name='Başlık Ekleyin')),
                ('titleiki', models.CharField(blank=True, max_length=500, verbose_name='Başlık  Ekleyin')),
                ('paragraf', models.CharField(blank=True, max_length=500, verbose_name='Açıklama Ekleyin')),
            ],
            options={
                'verbose_name': 'Kahve Agacı Açıklaması',
                'verbose_name_plural': 'Kahve Agacı Açıklaması',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='İnspectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('inspectmodel', models.ForeignKey(on_delete=anasayfa.models.İnspectModel, related_name='images', to='anasayfa.i̇nspectmodel')),
            ],
        ),
    ]
