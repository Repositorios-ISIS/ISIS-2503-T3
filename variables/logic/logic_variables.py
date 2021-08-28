# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 07:41:03 2021

@author: user
"""

from ..models import Variable

def get_all_variables():
    variables = Variable.objects.all()
    return variables