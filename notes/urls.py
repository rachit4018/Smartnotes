from django.urls import path
from . import views
from .views import NotesCreatView,NotesUpadteView
#urlconfig
urlpatterns = [
    path('notes/', views.list),
    path('notes/<int:pk>', views.detail, name='notes.details'),
    path('notes/<int:pk>/edit', views.NotesUpadteView.as_view(), name='notes.update'),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name='notes.delete'),
    path('notes/new', views.NotesCreatView.as_view(), name='notes.new'),
    path('notes/list', views.list, name='notes.list'),

]