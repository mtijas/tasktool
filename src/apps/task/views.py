# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.views.generic.list import ListView

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import Task
from .forms import TaskForm, TaskEditForm


def list_tasks(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'task/task_list.html', {'tasks': tasks})

def get_table(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'task/task_table.html', {'tasks': tasks})

class TaskCreateView(View):
    def get(self, request):
        form = TaskForm()
        return render(request, 'task/task_form.html', {'form': form})

    def post(self, request):
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
        return response

class TaskModifyView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        form = TaskEditForm(initial={'title': task.title, 'description': task.description})
        return render(request, 'task/task_edit_form.html', {'form': form, 'task': task})

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
        return render(request, 'task/task_edit_form.html', {'form': form, 'task': task})

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
