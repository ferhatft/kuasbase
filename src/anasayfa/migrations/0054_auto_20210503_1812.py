# Generated by Django 3.1.1 on 2021-05-03 15:12

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0053_auto_20210503_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whatwedomodel',
            name='paragrafbir',
        ),
        migrations.RemoveField(
            model_name='whatwedomodel',
            name='paragrafiki',
        ),
        migrations.RemoveField(
            model_name='whatwedomodel',
            name='paragrafüç',
        ),
        migrations.AddField(
            model_name='whatwedomodel',
            name='richtext',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name="ek metin '18' "),
        ),
        migrations.AlterField(
            model_name='whatwedomodel',
            name='main_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name="Fotoğraf '16'"),
        ),
        migrations.AlterField(
            model_name='whatwedomodel',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, verbose_name="Altbaşlık '17'"),
        ),
        migrations.AlterField(
            model_name='whatwedomodel',
            name='title',
            field=models.CharField(blank=True, max_length=500, verbose_name="Başlık '15'"),
        ),
        migrations.AlterField(
            model_name='whatwedomodel',
            name='video',
            field=models.CharField(blank=True, max_length=500, verbose_name="Video iframe linki Ekleyin '19' "),
        ),
        migrations.AlterField(
            model_name='whowearemodel',
            name='main_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name="Fotoğraf '11' "),
        ),
        migrations.AlterField(
            model_name='whowearemodel',
            name='richtext',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name="ek metin '14' "),
        ),
        migrations.AlterField(
            model_name='whowearemodel',
            name='sub_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name="Fotoğrafı '13'"),
        ),
        migrations.AlterField(
            model_name='whowearemodel',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, verbose_name="Alt başlık '12' "),
        ),
        migrations.AlterField(
            model_name='whowearemodel',
            name='title',
            field=models.CharField(blank=True, max_length=500, verbose_name="Başlık '10' "),
        ),
    ]
