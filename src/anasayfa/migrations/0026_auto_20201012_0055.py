# Generated by Django 3.1.1 on 2020-10-11 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0025_mediafile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mediafile',
            old_name='file',
            new_name='image',
        ),
    ]
