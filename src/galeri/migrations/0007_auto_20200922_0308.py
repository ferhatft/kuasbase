# Generated by Django 3.1.1 on 2020-09-22 00:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeri', '0006_auto_20200922_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galerimodel',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='açıklama üç'),
        ),
    ]