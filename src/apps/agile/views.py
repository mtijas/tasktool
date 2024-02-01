# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.views.generic.list import ListView

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from .epic.models import Epic

from .theme.models import Theme

@login_required
@permission_required('agile.view_agile')
def dashboard(request):
    themes = Theme.objects.order_by('title')
    return render(request, 'agile/dashboard.html', {'themes': themes})

@login_required
@permission_required('agile.view_agile')
def get_dashboard_themes(request):
    themes = Theme.objects.order_by('title')
    return render(request, 'agile/dashboard-themes.html', {'themes': themes})

@login_required
@permission_required('agile.view_agile')
def get_dashboard_epics(request, theme_id):
    epics = Epic.objects.filter(themes__id=theme_id).all()
    return render(request, 'agile/dashboard-epics.html', {'epics': epics, 'theme_id': theme_id})

