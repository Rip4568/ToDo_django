from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View,TemplateView

from .models import Task
from .forms import TaskForm

class TaskTemplateView(TemplateView):
    template_name = 'Task_app/task_list.html'

class TaskView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        tasks = Task.objects.all()
        context = {
            'request':request,
            'form':form,
            'tasks':tasks,
        }
        return render(request,'Task_app/task_list.html',context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        
        if form.is_valid():
            new_task = form.save()
            return redirect('Task_app:home')
        else:
            return redirect('Task_app:home')
