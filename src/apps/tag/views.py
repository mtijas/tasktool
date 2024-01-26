# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.views.generic.list import ListView

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Tag
from .forms import TagEditForm

@login_required
@permission_required('tag.view_tag')
def list_tags(request):
    tags = Tag.objects.order_by('title')
    return render(request, 'tag/tag_table.html', {'tags': tags})

@login_required
@permission_required('tag.view_tag')
def get_table(request):
    tags = Tag.objects.order_by('title')
    return render(request, 'tag/table_rows.html', {'tags': tags})

class TagCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'tag.add_tag'

    def get(self, request):
        form = TagEditForm(initial={'background_color': '#000000', 'text_color': '#ffffff'})
        return render(request, 'tag/quick_edit_form.html', {'form': form})

    def post(self, request):
        form = TagEditForm(request.POST)
        if form.is_valid():
            tag = Tag()
            tag.title = form.cleaned_data['title']
            tag.background_color = form.cleaned_data['background_color']
            tag.text_color = form.cleaned_data['text_color']
            tag.save()
            response = render(request, 'common/close_modal.html')
            response['HX-Trigger'] = 'newTag'
        else:
            response = render(request, 'tag/quick_edit_form.html', {'form': form})
        return response

class TagUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'tag.change_tag'

    def get(self, request, tag_id):
        tag = get_object_or_404(Tag, pk=tag_id)
        form = TagEditForm(initial={'title': tag.title, 'background_color': tag.background_color, 'text_color': tag.text_color})
        return render(request, 'tag/quick_edit_form.html', {'form': form, 'tag': tag})

    def post(self, request, tag_id):
        tag = get_object_or_404(Tag, pk=tag_id)
        form = TagEditForm(request.POST)
        if form.is_valid():
            tag.title = form.cleaned_data['title']
            tag.background_color = form.cleaned_data['background_color']
            tag.text_color = form.cleaned_data['text_color']
            tag.save()
            response = render(request, 'common/close_modal.html')
            response['HX-Trigger'] = 'newTag'
            return response
        return render(request, 'tag/quick_edit_form.html', {'form': form, 'tag': tag})

class TagDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'tag.delete_tag'

    def delete(self, request, tag_id):
        Tag.objects.filter(pk=tag_id).delete()
        return HttpResponse(status=200)
