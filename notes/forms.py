from django import forms
from .models import Note
from django.core.exceptions import ValidationError

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
    
    def clean_title(self):
        title = self.cleaned_data['title']
        return title