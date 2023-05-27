from django.shortcuts import render
from clinicalapp.models import ClinicalData, Patient
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from clinicalapp.forms import ClinicalDataForm
from django.shortcuts import redirect


# Create your views here.


class PatientListView(ListView):
    model = Patient
    # default template_name is patient_list.html which it will generated
    # to change the template name template_name = '' 
    # default context_object_name is patient


class PatientCreateView(CreateView):
    model = Patient
    # to reload back to homepage
    success_url = reverse_lazy('index')
    # to specify the field you want to create
    fields = ('firstName', 'lastName', 'age')
    # html template name patient_form.html


class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstName', 'lastName', 'age')


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')

    # student_confirm_delete.html

    # before you make migration make sure you create database

    # class base view


def addData(request, **kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'clinicalapp/clinicaldata_form.html', {'form': form, 'patient': patient})


# we need to pass in the patient id that why we insect kwargs
def analyze(request, **kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData = []
    for eachEntry in data:
        if eachEntry.componentName == 'hw':
            heightAndWeight = eachEntry.componentValue.split('/')
            if len(heightAndWeight) > 1:
                feetToMeters = float(heightAndWeight[0]) * 0.04536
                BMI = (float(heightAndWeight[1])) / (feetToMeters * feetToMeters)
                bmiEntry = ClinicalData()
                bmiEntry.componentName = 'BMI'
                bmiEntry.componentValue = BMI
                responseData.append(bmiEntry)
        responseData.append(eachEntry)
    return render(request, 'clinicalapp/generateReport.html', {'data': responseData})
