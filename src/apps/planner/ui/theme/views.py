# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.views.generic.list import ListView

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from ...models.theme import Theme
from .forms import ThemeEditForm

@login_required
@permission_required('theme.view_theme')
def list_themes(request):
    themes = Theme.objects.order_by('title')
    return render(request, 'planner/theme/theme_table.html', {'themes': themes})

@login_required
@permission_required('theme.view_theme')
def get_table(request):
    themes = Theme.objects.order_by('title')
    return render(request, 'planner/theme/table_rows.html', {'themes': themes})

class ThemeCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'theme.add_theme'

    def get(self, request):
        form = ThemeEditForm()
        return render(request, 'planner/theme/quick_edit_form.html', {'form': form})

    def post(self, request):
        form = ThemeEditForm(request.POST)
        if form.is_valid():
            theme = Theme()
            theme.title = form.cleaned_data['title']
            theme.description = form.cleaned_data['description']
            theme.save()
            response = render(request, 'common/close_modal.html')
            response['HX-Trigger'] = 'newTheme'
        else:
            response = render(request, 'planner/theme/quick_edit_form.html', {'form': form})
        return response

class ThemeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'theme.change_theme'

    def get(self, request, theme_id):
        theme = get_object_or_404(Theme, pk=theme_id)
        form = ThemeEditForm(initial={'title': theme.title, 'description': theme.description})
        return render(request, 'planner/theme/quick_edit_form.html', {'form': form, 'theme': theme})

    def post(self, request, theme_id):
        theme = get_object_or_404(Theme, pk=theme_id)
        form = ThemeEditForm(request.POST)
        if form.is_valid():
            theme.title = form.cleaned_data['title']
            theme.description = form.cleaned_data['description']
            theme.save()
            response = render(request, 'common/close_modal.html')
            response['HX-Trigger'] = 'newTheme'
            return response
        return render(request, 'planner/theme/quick_edit_form.html', {'form': form, 'theme': theme})

class ThemeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'theme.delete_theme'

    def delete(self, request, theme_id):
        Theme.objects.filter(pk=theme_id).delete()
        return HttpResponse(status=200)
