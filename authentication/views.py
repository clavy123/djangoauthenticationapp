from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .forms import AuthenticationForm
from django.contrib import messages
def home(request):
    return render(request,"home.htm")
def register(request):
    if request.method=='POST':
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,"account is created"+username)
            return redirect("login")
    else:
        form=AuthenticationForm()
    return render(request,'register.htm',{'form':form})
def logins(request):
    if request.method=='POST':
        users=request.POST['num1']
        password=request.POST['num2']
        user=authenticate(request,username=users,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
         
    return render(request,'login.htm')
def logouts(request):
    logout(request)
    return redirect("login")
def order(request):
    return render(request,'order.htm')