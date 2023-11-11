from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Note
from django.http import Http404,HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import NoteForm
from django.views.generic.edit import DeleteView

class HomeView(TemplateView):
    template_name = 'notes.html'
    all_notes = Note.objects.all()
    extra_content = {'notes': all_notes}

class NotesListView(LoginRequiredMixin, ListView):
    model =  Note
    context_object_name = "notes"
    template_name = "notes_list.html"
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

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

class NotesCreatView(LoginRequiredMixin, CreateView):
    model =  Note
    template_name = 'notes_form.html'
    #fields = ['title','text']
    form_class = NoteForm
    success_url = reverse_lazy('notes.list')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())




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

