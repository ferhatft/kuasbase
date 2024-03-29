# Generated by Django 3.1.1 on 2021-05-04 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeri', '0016_auto_20210504_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galerimodel',
            name='main_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name="Ana fotoğraf '1920x900'"),
        ),
        migrations.AlterField(
            model_name='galerimodel',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Alt başlık'),
        ),
        migrations.AlterField(
            model_name='galerimodel',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Başlık '),
        ),
    ]
