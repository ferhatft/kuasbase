# Generated by Django 3.1.1 on 2020-09-23 20:32

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blogmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimage',
            name='inspectmodel',
            field=models.ForeignKey(on_delete=blog.models.BlogModel, related_name='imageswithcontext', to='blog.blogmodel'),
        ),
        migrations.AlterField(
            model_name='blogonlyimage',
            name='inspectmodel',
            field=models.ForeignKey(on_delete=blog.models.BlogModel, related_name='images', to='blog.blogmodel'),
        ),
    ]