# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.apps import apps
from forms import *
from models import *

@login_required
def home(request):
    return render(request,"home.html")

@login_required
def house(request):
    if request.method == 'POST':
        # import ipdb;ipdb.set_trace()
        # request.POST["user_id"] = request.user.id
        house_form = HouseForm(request.POST, request.FILES)
        if house_form.is_valid():
            house = house_form.save()
            house.user = request.user
            house.save()
            return redirect('/house/list')
        else:
            return render(request, 'houseform.html', {'form': house_form})
    else:
        house_form = HouseForm()
        return render(request, 'houseform.html', {'form': house_form})

@login_required
def house_list(request):
    houses = House.objects.filter(user=request.user)

    if request.GET.get("swimming_pool"):
        houses = houses.filter(swimming_pool=True)
    if request.GET.get("pets_allowed"):
        houses = houses.filter(pets_allowed=True)

    data = {}
    data["houses"] = houses

    return render(request, "house_list.html", data)
