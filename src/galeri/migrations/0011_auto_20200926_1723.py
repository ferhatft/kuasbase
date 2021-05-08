# Generated by Django 3.1.1 on 2020-09-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeri', '0010_auto_20200926_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='galerimodel',
            name='main_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Ana Sayfa fotoğrafı'),
        ),
        migrations.AddField(
            model_name='galerimodel',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Alt başlık ekleyin'),
        ),
        migrations.AlterField(
            model_name='galerimodel',
            name='paragrafbir',
            field=models.CharField(blank=True, max_length=500, verbose_name='Kısa açıklama ekleyin'),
        ),
        migrations.AlterField(
            model_name='galerimodel',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Başlık ekleyin'),
        ),
    ]
