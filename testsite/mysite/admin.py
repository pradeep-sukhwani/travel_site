# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.

class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'city', 'available_from', 'available_till', 'amount', 'sleep', 'swimming_pool', 'gym', 'pet_allowed', 'user')
    list_filter = ('city',)

admin.site.register(House, HouseAdmin)
admin.site.register(City)
