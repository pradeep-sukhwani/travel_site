# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0020_auto_20170413_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
