# Generated by Django 3.1.1 on 2020-09-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0003_auto_20200921_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='i̇nspectmodel',
            name='title',
            field=models.CharField(blank=True, max_length=500, verbose_name='Başlık bir'),
        ),
        migrations.AlterField(
            model_name='i̇nspectmodel',
            name='titleiki',
            field=models.CharField(blank=True, max_length=500, verbose_name='Başlık iki'),
        ),
    ]
