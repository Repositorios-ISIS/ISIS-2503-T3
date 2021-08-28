# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 06:09:36 2021

@author: user
"""

from django.urls import path
from . import views
from monitoring import views as views_monitoring

urlpatterns = [
    path('create_measurement/',views.create_measurement,name='create_measurement'),
    path('get_measurement/<int:identificador>',views.get_measurement,name='get_measurement'),
    path('update_measurement/<int:identificador>',views.update_measurement,name='update_measurement'),
    path('delete_measurement/<int:identificador>',views.delete_measurement,name='delete_measurement'),
    path('list/',views.list_measurements,name='list_measurements'),
    path('',views_monitoring.home,name='index')
]