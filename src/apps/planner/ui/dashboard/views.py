# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.views.generic.list import ListView

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from ...models.theme import Theme
from ...models.epic import Epic

@login_required
@permission_required('planner.view_planner')
def dashboard(request):
    themes = Theme.objects.order_by('title')
    return render(request, 'planner/dashboard/dashboard.html', {'themes': themes})

@login_required
@permission_required('planner.view_planner')
def get_dashboard_themes(request):
    themes = Theme.objects.order_by('title')
    return render(request, 'planner/dashboard/dashboard-themes.html', {'themes': themes})

@login_required
@permission_required('planner.view_planner')
def get_dashboard_epics(request, theme_id):
    theme = get_object_or_404(Theme, pk=theme_id)
    return render(request, 'planner/dashboard/dashboard-epics.html', {'theme': theme})

@login_required
@permission_required('planner.view_planner')
def get_dashboard_stories(request, epic_id):
    epic = get_object_or_404(Epic, pk=epic_id)
    return render(request, 'planner/dashboard/dashboard-stories.html', {'epic': epic})
