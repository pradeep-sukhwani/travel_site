# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_auto_20170411_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('AMD', 'Ahmedabad'), ('BOM', 'Mumbai'), ('PNQ', 'Pune'), ('GOI', 'Goa'), ('BLR', 'Bangalore'), ('MAA', 'Chennai'), ('DEL', 'Delhi'), ('COK', 'Cochin'), ('CCJ', 'Calicut'), ('VTZ', 'Visakhapatnam'), ('GAU', 'Guwahati'), ('PAT', 'Patna'), ('IXC', 'Chandigarh'), ('RPR', 'Raipur'), ('NMB', 'Daman'), ('DIU', 'Diu'), ('SLV', 'Shimla'), ('IXJ', 'Jammu and Kashmir'), ('IXL', 'Ladakh')], max_length=3, null='True')),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.AlterField(
            model_name='house',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mysite.City'),
        ),
    ]