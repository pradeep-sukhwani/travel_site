# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 08:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='is_gym',
            new_name='gym',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='is_pet_allowed',
            new_name='pet_allowed',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='rooms',
            new_name='room',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='is_swimming_pool',
            new_name='swimming_pool',
        ),
    ]
