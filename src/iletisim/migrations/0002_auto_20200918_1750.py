# Generated by Django 3.1.1 on 2020-09-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iletisim', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='i̇nfo',
            name='location',
            field=models.CharField(max_length=300, verbose_name='Adres'),
        ),
    ]