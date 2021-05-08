# Generated by Django 3.1.1 on 2020-09-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0017_whowearemodel_sub_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='onlycontext',
            options={'verbose_name': 'Ana sayfa paragraf ', 'verbose_name_plural': 'Ana sayfa paragraflat '},
        ),
        migrations.AlterField(
            model_name='onlycontext',
            name='context',
            field=models.CharField(max_length=500, verbose_name='Paragraf  ekleyin'),
        ),
        migrations.AlterField(
            model_name='whowearemodel',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, verbose_name='Alt başlık Ekleyin'),
        ),
    ]
