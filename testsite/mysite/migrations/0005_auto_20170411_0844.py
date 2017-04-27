# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20170411_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='house',
            name='start_date',
        ),
        migrations.AddField(
            model_name='house',
            name='amount',
            field=models.PositiveIntegerField(null=True, verbose_name='\u20b9'),
        ),
    ]
