from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from classBVapp.models import Student
from django.urls import reverse_lazy
# Create your views here.


class StudentListView(ListView):
    model = Student
    #default template_name is student_list.html which it will generated
    # to change the template name template_name = '' 
    #default context_object_name is student_list


class StudentDetails(DetailView):
    model = Student
    #default template_name is student_detail.html which it will generated
    # to change the template name template_name = '' 
    #default context_object_name is student 


class StudentCreateView(CreateView):
    model = Student
    fields = ('firstName', 'lastName', 'testScore')
     
    #default template_name is student_form.html which it will generated
    # to change the template name template_name = '' 
    #default context_object_name is student 


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('testScore',)

    #default template_name is student_form.html which it will generated
    # to change the template name template_name = '' 
    #default context_object_name is student 


class StudentDeleteView(DeleteView):
    model = Student
    # to redirect to home page
    success_url=reverse_lazy('students')
    
    #student_confirm_delete.html