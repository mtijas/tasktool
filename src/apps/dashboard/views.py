from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import ListView

from .models import Dashboard

class BaseDashboardView(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    model = Dashboard
    permission_required = 'dashboard.view_dashboard'
    template_name = 'dashboards/base_dashboard.html'