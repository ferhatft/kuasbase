# Generated by Django 3.1.1 on 2020-09-24 01:00

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200924_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogonlycontxt',
            name='inspectmodel',
            field=models.ForeignKey(on_delete=blog.models.BlogModel, related_name='context', to='blog.blogmodel'),
        ),
    ]