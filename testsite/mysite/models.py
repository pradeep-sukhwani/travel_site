# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

location = (  
    ('AMD', 'Ahmedabad'),
    ('BOM', 'Mumbai'),
    ('PNQ', 'Pune'),
    ('GOI', 'Goa'),
    ('BLR', 'Bangalore'),
    ('MAA', 'Chennai'),
    ('DEL', 'Delhi'),
    ('COK', 'Cochin'),
    ('CCJ', 'Calicut'),
    ('VTZ', 'Visakhapatnam'),
    ('GAU', 'Guwahati'),
    ('PAT', 'Patna'),
    ('IXC', 'Chandigarh'),
    ('RPR', 'Raipur'),
    ('NMB', 'Daman'),
    ('DIU', 'Diu'),
    ('SLV', 'Shimla'),
    ('IXJ', 'Jammu and Kashmir'),
    ('IXL', 'Ladakh'),
)

class City(models.Model):
    location = models.CharField(max_length=30, choices=location, null='True')

    def __unicode__(self):
        return dict(location).get(self.location)

    class Meta():
        verbose_name_plural = "cities"

def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)

class House(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField()
    available_from = models.DateField(null=True)
    available_till = models.DateField(null=True)
    user = models.ForeignKey(User, null=True)
    city = models.ForeignKey(City, null=True)
    location = models.CharField(max_length=128, null=True)
    amount = models.FloatField("Amount (in INR/night)")
    sleep = models.PositiveSmallIntegerField(default=1)
    bedroom = models.PositiveSmallIntegerField(default=1)
    bathroom = models.PositiveSmallIntegerField(default=1)
    power_backup = models.BooleanField(default=False)
    television = models.BooleanField(default=False)
    spa = models.BooleanField(default=False)
    cook_on_call = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    house_keeping = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    non_veg = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)
    smoke = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    pet_allowed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title
