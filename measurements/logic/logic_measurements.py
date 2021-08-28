# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 07:27:37 2021

@author: user
"""

from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(identificador):
    measurement = Measurement.objects.get(id = identificador)
    return measurement