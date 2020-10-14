from django.shortcuts import render
from .forms import TaskForm
from .models import Task


# Create your views here.



forms=[];
def save_list(request):
    for form in forms:
        if  form.is_valid() :


            f = Task.objects.create(title= form.cleaned_data)
            f.save()
            f.publish()

    return render(request, 'main/save.html', {'forms': Task.objects.all()}) # ищет в templates по дефолту




def task_add(request):

        forms.append(TaskForm()) ;
        return render(request, 'main/task_add.html', {'forms': forms})
