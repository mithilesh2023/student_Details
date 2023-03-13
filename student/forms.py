from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class ApplyForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class RegisterForm(UserCreationForm):
    name=forms.CharField(max_length=200)
    mobile=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=200)
        