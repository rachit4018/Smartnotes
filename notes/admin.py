from django.contrib import admin
from . import models
# Register your models here.
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title',)

# to register the model and class in admin site
admin.site.register(models.Note, NoteAdmin)