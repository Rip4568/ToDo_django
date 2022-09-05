#create your custom forms here

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("titulo",)

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
        }