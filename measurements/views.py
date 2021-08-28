from django.shortcuts import render, redirect

# Create your views here.

from .models import *
from .forms import MeasurementForm
from .logic import logic_measurements
from django.core import serializers
from django.http import HttpResponse
import json

def create_measurement(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MeasurementForm()
    return render(request, 'create_update_measurement.html', {'form':form})

def list_measurements(request):
    measurements = logic_measurements.get_all_measurements()
    measurements_list = serializers.serialize('json',measurements)
    measurements_list = json.loads(measurements_list)
    return render(request, 'list_measurements.html', {'measurements':measurements_list})

def update_measurement(request,identificador):
    measurement = logic_measurements.get_measurement(identificador)
    if request.method == 'GET':
        form = MeasurementForm(instance = measurement)
    else:
        form = MeasurementForm(request.POST, instance = measurement)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'create_update_measurement.html', {'form':form})

def delete_measurement(request, identificador):
    measurement = logic_measurements.get_measurement(identificador)
    if request.method == 'POST':
        measurement.delete()
        return redirect("index")
    return render(request, 'delete_measurement.html', {'measurement':measurement})

def get_measurement(request, identificador):
    measurement = logic_measurements.get_measurement(identificador)
    measurement = serializers.serialize('json', [measurement,])
    return render(request, 'get_measurement.html', {'measurement':measurement,"id":identificador})