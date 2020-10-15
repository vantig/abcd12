from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']

 #title = forms.CharField(max_length=50);


def save(self):
    new_task = Task.objects.create(self.title)
    return new_task;
