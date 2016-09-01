from django.shortcuts import render
from django.http import HttpResponse
from .models import MachineStatus

def index(request): 
    machine_list = MachineStatus.objects.values()   
    context = {"machine_list": machine_list} 
    return render(request, "machineStatus/index.html", context)  

def results(response, machine_id): 
    response = "You are looking at Machine %s"
    return HttpResponse(response % machine_id) 
