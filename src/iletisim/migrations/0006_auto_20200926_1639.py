# Generated by Django 3.1.1 on 2020-09-26 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iletisim', '0005_auto_20200926_1638'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='i̇nfo',
            options={'ordering': ['email'], 'verbose_name': 'Şirket  Bilgisi', 'verbose_name_plural': 'Şirket  Bilgileri'},
        ),
    ]