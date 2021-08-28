# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 07:49:38 2021

@author: user
"""

from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.get_variables,name='variableList')    
]