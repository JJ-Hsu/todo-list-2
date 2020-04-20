from django import forms
from . import models

class CreateTask(forms.ModelForm):
    class Meta: #metadata
        model = models.Task
        fields = ['title',]
