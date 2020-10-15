from django.shortcuts import render
from .forms import TaskForm
from .models import Task


# Create your views here.


def task_add(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TaskForm();
    context = {
        'form': form
    }
    return render(request, 'main/task_add.html', context)


def save_list(request):
    return render(request, 'main/save.html', {'forms': Task.objects.all()})  # ищет в templates по дефолту
