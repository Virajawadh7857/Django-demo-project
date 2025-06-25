from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.

def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,('New Task Added!'))
            return redirect('todolist')
        else:
            return redirect('todolist')
    else:
        all_task = TaskList.objects.all()
        paginator = Paginator(all_task, 6)
        Page = request.GET.get('pg')
        all_task = paginator.get_page(Page)
        return render(request, 'todolist.html',{'all_task':all_task})

def about(request):
    return render(request, 'about.html',{})

def contact(request):
    return render(request, 'contact.html',{})



def delete_task(request,task_id):
    task = TaskList.objects.get(id=task_id)
    task.delete()
    messages.info(request, ('deleted!'))
    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == 'POST':
        task = TaskList.objects.get(id=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request,('Task Edited!'))
        return redirect('todolist')

    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html',{'task_obj':task_obj})



def complete_task(request,task_id):
    task = TaskList.objects.get(id=task_id)
    task.done = True
    task.save()
    return redirect('todolist')

def pending_task(request,task_id):
    task = TaskList.objects.get(id=task_id)
    task.done = False
    task.save()
    return redirect('todolist')

