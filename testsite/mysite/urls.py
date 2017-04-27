from django.conf.urls import url
from views import *

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^house/add', house, name='house'),
    url(r'^house/list', house_list, name='house_list'),
]
