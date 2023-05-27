from django.shortcuts import render
from . import form

# Create your views here.

def userRegistrationView(request):
    forms = form.UserRegistrationForm()
    if request.method=='POST':
        forms=form.UserRegistrationForm(request.POST)
        if forms.is_valid():
            print("Form is Valid")
            print("First Name", forms.cleaned_data['firstname'])
            print("Last Name", forms.cleaned_data['lastname'])
            print("Email", forms.cleaned_data['email'])
    return render(request, 'form.html', {'forms': forms})