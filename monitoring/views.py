# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 07:33:03 2021

@author: user
"""

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')