# Generated by Django 3.1.1 on 2020-09-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorular', '0002_auto_20200923_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='sorumodel',
            name='pagetitle',
            field=models.CharField(max_length=500, null=True, verbose_name='sayfa ana başlığı ekleyin'),
        ),
    ]
