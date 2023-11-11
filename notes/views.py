from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Note
from django.http import Http404
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import NoteForm
from django.views.generic.edit import DeleteView

class HomeView(TemplateView):
    template_name = 'notes.html'
    all_notes = Note.objects.all()
    extra_content = {'notes': all_notes}

class NotesDeleteView(DeleteView):
    model = Note
    template_name='notes_delete.html'
    success_url = reverse_lazy('notes.list')

class NotesUpadteView(UpdateView):
    model =  Note
    template_name = 'notes_form.html'
    #fields = ['title','text']
    form_class = NoteForm
    success_url = reverse_lazy('notes.list')

class NotesCreatView(CreateView):
    model =  Note
    template_name = 'notes_form.html'
    #fields = ['title','text']
    form_class = NoteForm
    success_url = reverse_lazy('notes.list')

#Commenting because we are using templateview for views (The above HomeView template class)    
def list(request):
    all_notes = Note.objects.all()
    return render(request, 'notes.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        raise Http404(" Note Doesnot Exist")

    return render(request, 'notes_details.html', {'notes': note})

