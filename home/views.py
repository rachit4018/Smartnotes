from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def calculate():
    x = 1
    return x
def home(request):
    x = calculate()
    return render(request, 'home.html', {'name':'Rachit'})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'authorized.html',{})