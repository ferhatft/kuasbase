# Generated by Django 3.1.1 on 2020-09-26 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0019_auto_20200927_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='KuasLogoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(upload_to='', verbose_name='Şirket Logosu Ekleyin ')),
            ],
            options={
                'verbose_name': 'Şirket Logosu',
                'verbose_name_plural': 'Şirket Logosu',
                'ordering': ['logo'],
            },
        ),
    ]