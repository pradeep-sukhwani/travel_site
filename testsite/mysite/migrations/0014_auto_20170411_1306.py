# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 13:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20170411_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='location',
            new_name='locations',
        ),
    ]
