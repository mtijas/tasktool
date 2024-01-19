# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.views.generic.list import ListView

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Task
from .forms import TaskForm


def list_tasks(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'task/task_list.html', {'tasks': tasks})

def get_table(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'task/task_table.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task()
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.save()
            response = render(request, 'task/new_task_button.html', {'task': task})
            response['HX-Trigger'] = 'newTask'
        else:
            response = render(request, 'task/task_form.html', {'form': form})
    else:
        form = TaskForm()
        response = render(request, 'task/task_form.html', {'form': form})

    return response

class TaskView(View):
    def delete(self, request, task_id):
        Task.objects.filter(pk=task_id).delete()
        return HttpResponse(status=200)

# class TaskListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
#     model = Task
#     permission_required = 'task.view_task'
#     template_name = 'task/task_list.html'


# class TaskCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
#     model = Task
#     permission_required = 'task.add_task'
#     success_url = reverse_lazy('task-list')
#     template_name = 'task/task_form.html'
#     form_class = TaskForm


# class TaskUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
#     model = Task
#     permission_required = 'task.change_task'
#     template_name = 'task/task_update_form.html'
#     success_url = reverse_lazy('task-list')
#     form_class = TaskForm


# class TaskDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
#     model = Task
#     permission_required = 'task.delete_task'
#     success_url = reverse_lazy('task-list')
#     template_name = 'task/task_confirm_delete.html'
