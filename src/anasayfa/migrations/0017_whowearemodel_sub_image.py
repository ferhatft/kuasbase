# Generated by Django 3.1.1 on 2020-09-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0016_auto_20200924_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='whowearemodel',
            name='sub_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Alt Fotoğrafı Ekleyin'),
        ),
    ]
