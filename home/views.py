from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
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

class LoginInterfaceView(LoginView):
    template_name = "login.html"

class LogoutInterfaceView(LogoutView):
    template_name = "logout.html"

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)
        