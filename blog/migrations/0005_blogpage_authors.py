# Generated by Django 5.0.3 on 2024-10-20 13:08

import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='authors',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.author'),
        ),
    ]
