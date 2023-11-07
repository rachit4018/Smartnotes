from django.shortcuts import render
from .models import Note
# Create your views here.

def list(request):
    all_notes = Note.objects.all()
    return render(request, 'notes.html', {'notes': all_notes})

