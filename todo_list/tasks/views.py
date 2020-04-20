from django.shortcuts import render, redirect
from . models import Task
from . import forms

# Create your views here.
def task_list(request):

    if request.method == 'POST':

        # CHECK IF IT'S DELETE
        if len(request.POST) == 2 and 'title' not in request.POST:
            delete_task(request)
            return redirect('tasks:task_list')
        # IF NOT DELETE, THEN CREATE
        else:
            create_task(request)
            return redirect('tasks:task_list')
    else:
        form = forms.CreateTask()

    # LIST TASKS
    tasks = Task.objects.all().order_by('date').reverse()
    return render(request, "tasks/task_list.html", {'tasks': tasks, 'form':form})

def create_task(request):
    form = forms.CreateTask(request.POST)
    if form.is_valid():
        form.save()

def delete_task(request):
    key_list = []
    for key in request.POST.keys():
        key_list.append(key)
    task_name = key_list[1]
    Task.objects.get(title=task_name).delete()
