# Generated by Django 3.1.1 on 2021-05-01 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0045_auto_20201012_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='i̇nspectmodel',
            name='contextmain',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name="açıklama '2' "),
        ),
        migrations.AlterField(
            model_name='i̇nspectmodel',
            name='formcontext',
            field=models.CharField(blank=True, max_length=500, verbose_name="form açıklama '4' "),
        ),
        migrations.AlterField(
            model_name='i̇nspectmodel',
            name='formtitle',
            field=models.CharField(blank=True, max_length=500, verbose_name="form başlık  '3' "),
        ),
        migrations.AlterField(
            model_name='i̇nspectmodel',
            name='main_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Arka plan '),
        ),
        migrations.AlterField(
            model_name='i̇nspectmodel',
            name='title',
            field=models.CharField(blank=True, max_length=500, verbose_name="Başlık '1' "),
        ),
    ]
