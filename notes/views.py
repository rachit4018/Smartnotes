from django.shortcuts import render
from .models import Note
from django.http import Http404
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'notes.html'
    all_notes = Note.objects.all()
    extra_content = {'notes': all_notes}


# Commenting because we are using templateview for views (The above HomeView template class)    
# def list(request):
#     all_notes = Note.objects.all()
#     return render(request, 'notes.html', {'notes': all_notes})


def detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        raise Http404(" Note Doesnot Exist")

    return render(request, 'notes_details.html', {'notes': note})

