from django.shortcuts import render


# Create your views here.


def renderTemplates(request):
    mydit = {"name": "Bolarinwa"}
    return render(request, 'templatesApp/index.html', context=mydit)


def renderEmployeee(request):
    myDict = {"id": 123, "name": "John", "sal": 10000}
    return render(request, "templatesApp/employeetemplates.html", myDict)


