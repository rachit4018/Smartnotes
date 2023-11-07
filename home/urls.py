from django.urls import path
from . import views
import debug_toolbar


#urlconfig
urlpatterns = [
    path('home/', views.home),
    path('authorized/', views.authorized),
]