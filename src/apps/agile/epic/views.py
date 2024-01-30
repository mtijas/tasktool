# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.views.generic.list import ListView

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from ..theme.models import Theme

from .models import Epic
from .forms import EpicEditForm

@login_required
@permission_required('epic.view_epic')
def list_epics(request):
    epics = Epic.objects.order_by('title')
    return render(request, 'agile/epic/epic_table.html', {'epics': epics})

@login_required
@permission_required('epic.view_epic')
def get_table(request):
    epics = Epic.objects.order_by('title')
    return render(request, 'agile/epic/table_rows.html', {'epics': epics})

class EpicCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'epic.add_epic'

    def get(self, request, theme_id=None):
        themes = [(t.id, t.title) for t in Theme.objects.all()]
        initial_themes = [theme_id]
        form = EpicEditForm(initial={'themes': initial_themes}, themes=themes)
        return render(request, 'agile/epic/quick_edit_form.html', {'form': form})

    def post(self, request):
        themes = [(t.id, t.title) for t in Theme.objects.all()]
        form = EpicEditForm(request.POST, themes=themes)
        if form.is_valid():
            epic = Epic()
            epic.title = form.cleaned_data['title']
            epic.description = form.cleaned_data['description']
            epic.save()
            epic.themes.set(form.cleaned_data['themes'])
            epic.save()
            response = render(request, 'common/close_modal.html')
            trigger_events = ['reloadAllEpics']
            for theme in form.cleaned_data['themes']:
                trigger_events.append(f'reloadEpics-{theme}')
            response['HX-Trigger'] = ", ".join(trigger_events)
        else:
            response = render(request, 'agile/epic/quick_edit_form.html', {'form': form})
        return response

class EpicUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'epic.change_epic'

    def get(self, request, epic_id):
        epic = get_object_or_404(Epic, pk=epic_id)
        themes = [(t.id, t.title) for t in Theme.objects.all()]
        initial_themes = [t.id for t in epic.themes.all()]
        form = EpicEditForm(initial={'title': epic.title, 'description': epic.description, 'themes': initial_themes}, themes=themes)
        return render(request, 'agile/epic/quick_edit_form.html', {'form': form, 'epic': epic})

    def post(self, request, epic_id):
        epic = get_object_or_404(Epic, pk=epic_id)
        themes = [(t.id, t.title) for t in Theme.objects.all()]
        form = EpicEditForm(request.POST, themes=themes)
        if form.is_valid():
            epic.title = form.cleaned_data['title']
            epic.description = form.cleaned_data['description']
            epic.themes.set(form.cleaned_data['themes'])
            epic.save()
            response = render(request, 'common/close_modal.html')
            response['HX-Trigger'] = 'reloadAllEpics'
            return response
        return render(request, 'agile/epic/quick_edit_form.html', {'form': form, 'epic': epic})

class EpicDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'epic.delete_epic'

    def delete(self, request, epic_id):
        Epic.objects.filter(pk=epic_id).delete()
        return HttpResponse(status=200)
