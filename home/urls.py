from django.urls import path
from . import views

#urlconfig
urlpatterns = [
    path('home/', views.home)
]