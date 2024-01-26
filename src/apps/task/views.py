# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.views.generic.list import ListView

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Task
from .forms import TaskEditForm

@login_required
@permission_required('task.view_task')
def list_tasks(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'task/task_table.html', {'tasks': tasks})

@login_required
@permission_required('task.view_task')
def get_table(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'task/table_rows.html', {'tasks': tasks})

class TaskCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'task.add_task'

    def get(self, request):
        form = TaskEditForm()
        return render(request, 'task/quick_edit_form.html', {'form': form})

    def post(self, request):
        form = TaskEditForm(request.POST)
        if form.is_valid():
            task = Task()
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.save()
            response = render(request, 'common/close_modal.html')
            response['HX-Trigger'] = 'newTask'
        else:
            response = render(request, 'task/quick_edit_form.html', {'form': form})
        return response

class TaskUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'task.change_task'

    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        form = TaskEditForm(initial={'title': task.title, 'description': task.description})
        return render(request, 'task/quick_edit_form.html', {'form': form, 'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        form = TaskEditForm(request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.save()
            response = render(request, 'common/close_modal.html')
            response['HX-Trigger'] = 'newTask'
            return response
        return render(request, 'task/quick_edit_form.html', {'form': form, 'task': task})

class TaskDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'task.delete_task'

    def delete(self, request, task_id):
        Task.objects.filter(pk=task_id).delete()
        return HttpResponse(status=200)
