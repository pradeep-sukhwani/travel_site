# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 08:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0022_auto_20170414_0640'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['city', 'swimming_pool', 'gym', 'pet_allowed']},
        ),
    ]