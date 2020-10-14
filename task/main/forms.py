from django import forms
from .models import Task


class TaskForm(forms.Form):
  #   title = forms.CharField(max_length=50);

     class Meta:
         model = Task
         field = ('title')
     def save(self):
        new_task = Task.object.create(title=self.cleaned_data['title'])
        return new_task;

