# Generated by Django 3.1.1 on 2020-09-27 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0020_kuaslogomodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referansimage',
            name='referansmodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='anasayfa.referansmodel'),
        ),
    ]
