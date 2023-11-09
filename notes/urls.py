from django.urls import path
from . import views
from .views import NotesCreatView
#urlconfig
urlpatterns = [
    path('notes/', views.list),
    path('notes/<int:pk>', views.detail),
    path('notes/new', views.NotesCreatView.as_view(), name='notes.new'),
    path('notes/list', views.list),

]