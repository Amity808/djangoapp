from django.db import models


# Create your models here.

class Patient(models.Model):
    lastName = models.CharField(max_length=15)
    firstName = models.CharField(max_length=15)
    age = models.IntegerField()


class ClinicalData(models.Model):
    # to make a dropdown 
    COMPONENT_NAMES = [('hw', 'Height/Weight'), ('bp', 'Blood Pressure'), ('heartrate', 'Heart Rate')]
    componentName = models.CharField(choices=COMPONENT_NAMES, max_length=25)
    componentValue = models.CharField(max_length=25)
    # to get the current time or date use auto_now_add
    measureDateTime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
