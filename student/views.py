from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login as loginfun,logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

# Create your views here.
def homepage(r):
    data={}
    data['student']=Student.objects.all()
    return render(r, 'index.html',data)

def apply(r):
    form=ApplyForm(r.POST or None)
    if r.method=='POST':
        if form.is_valid():
            form.save()
            return redirect(homepage)
    return render(r, 'apply.html',{'form':form})

def register(r):
    form=RegisterForm(r.POST or None)
    if r.method=='POST':
        if form.is_valid():
           form.save()
           return redirect(login)
    return render(r, 'register.html',{'form':form})

def login(r):
    LoginForm=AuthenticationForm(r.POST or None, r.FIELS or None)
    if r.method=='POST':
        if LoginForm.is_valid():
            username=LoginForm.cleaned_data.get('username')
            password=LoginForm.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                loginfun(r, user)
                return redirect(homepage)
            else :
                return redirect(login)
    return render(r, 'login.html',{"form":LoginForm})

def logoutFunction(r):
    logout(r)
    return redirect(login)
@login_required()
def editStudent(r):
    return render(r,'admin/edit.html')