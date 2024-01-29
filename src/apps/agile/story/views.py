# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.views.generic.list import ListView

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from .models import Story
from .forms import StoryEditForm

@login_required
@permission_required('story.view_story')
def list_stories(request):
    stories = Story.objects.order_by('title')
    return render(request, 'agile/story/story_table.html', {'stories': stories})

@login_required
@permission_required('story.view_story')
def get_table(request):
    stories = Story.objects.order_by('title')
    return render(request, 'agile/story/table_rows.html', {'stories': stories})

class StoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'story.add_story'

    def get(self, request):
        form = StoryEditForm(initial={'background_color': '#000000', 'text_color': '#ffffff'})
        return render(request, 'agile/story/quick_edit_form.html', {'form': form})

    def post(self, request):
        form = StoryEditForm(request.POST)
        if form.is_valid():
            story = Story()
            story.title = form.cleaned_data['title']
            story.save()
            response = render(request, 'common/close_modal.html')
            response['HX-Trigger'] = 'newStory'
        else:
            response = render(request, 'agile/story/quick_edit_form.html', {'form': form})
        return response

class StoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'story.change_story'

    def get(self, request, story_id):
        story = get_object_or_404(Story, pk=story_id)
        form = StoryEditForm(initial={'title': story.title})
        return render(request, 'agile/story/quick_edit_form.html', {'form': form, 'story': story})

    def post(self, request, story_id):
        story = get_object_or_404(Story, pk=story_id)
        form = StoryEditForm(request.POST)
        if form.is_valid():
            story.title = form.cleaned_data['title']
            story.save()
            response = render(request, 'common/close_modal.html')
            response['HX-Trigger'] = 'newStory'
            return response
        return render(request, 'agile/story/quick_edit_form.html', {'form': form, 'story': story})

class StoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'story.delete_story'

    def delete(self, request, story_id):
        Story.objects.filter(pk=story_id).delete()
        return HttpResponse(status=200)
