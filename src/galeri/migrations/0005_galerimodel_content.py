# Generated by Django 3.1.1 on 2020-09-21 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeri', '0004_auto_20200922_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='galerimodel',
            name='content',
            field=models.TextField(blank=True, max_length=500, verbose_name='açıklama üç'),
        ),
    ]
