from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculate():
    x = 1
    return x
def home(request):
    x = calculate()
    return render(request, 'home.html', {'name':'Rachit'})
