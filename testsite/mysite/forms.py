# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from models import *
from django.contrib.admin.widgets import AdminDateWidget

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        # widgets = {
        #     'available_from': forms.DateInput(attrs={'class':'datepicker'}),
        #     'available_till': forms.DateInput(attrs={'class':'datepicker'}),
        # }
        fields = ['title', 'description', 'image', 'city', 'location', 'available_from', 'available_till',
                  'amount', 'sleep', 'bedroom', 'bathroom' ,'swimming_pool', 'gym', 'pet_allowed', 'power_backup',
                  'television', 'spa', 'cook_on_call', 'parking', 'house_keeping', 'air_conditioning',
                  'internet', 'non_veg', 'alcohol', 'smoke']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
