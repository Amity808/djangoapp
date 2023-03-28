from django.shortcuts import render
from modelapp.models import Empolyee
from . import forms
# Create your views here.

def employeedata(request):
    employees = Empolyee.objects.all()
    employeeDict = {'employees': employees}
    return render(request, 'employees.html', employeeDict)


def userRegisterationView(request):
    pass