from django.urls import path
from . import views


#urlconfig
urlpatterns = [
    path('notes/', views.HomeView.as_view()),
    path('notes/<int:pk>', views.detail),

]