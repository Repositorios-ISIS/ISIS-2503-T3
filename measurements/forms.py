# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 05:57:57 2021

@author: user
"""

from django import forms
from .models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'variable',
            'value',
            'unit',
            'place'        
        ]