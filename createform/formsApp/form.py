from django import forms
# to use inbuilt form validation import validators from django from core or serach django validators
from django.core import validators

class UserRegistrationForm(forms.Form):
    GENDER = [('male', 'MALE'), ('female', 'FEMALE')] 
    # to create a dropdown
    # by default all field are required 
    firstname=forms.CharField(validators=[validators.MinLengthValidator(5), validators.MaxLengthValidator(20)])
    # to make field not required required=False
    lastname=forms.CharField(required=False)
    email=forms.CharField()
    comments=forms.CharField(widget=forms.Textarea)
    gender= forms.CharField(widget=forms.Select(choices=GENDER))
    # to make a password input
    password=forms.CharField(widget=forms.PasswordInput)
    
    ssn=forms.IntegerField()




    #using a sigle clean method
    #to get validation through all the input
"""    def clean(self):
        user_cleaned_data = super().clean()
        inputFirstName = user_cleaned_data['firstname']
        if len(inputFirstName) > 20:
            raise forms.ValidationError('The max length of firstname is 20 character')
        
"""
    # how to write a clean custom validation method in your code
    # to make max of only 30 characters input 
"""  def clean_firstname(self):
        inputFirstName = self.cleaned_data['firstname']
        if len(inputFirstName) > 20:
            raise forms.ValidationError('The max length of firstname is 20 character')
        return inputFirstName
    
    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@')==-1:
            raise forms.ValidationError('The email shouuld contain @')
        return inputEmail"""
    