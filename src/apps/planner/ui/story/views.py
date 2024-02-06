# from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.views.generic.list import ListView

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required

from ...models.epic import Epic
from ...models.story import Story
from .forms import StoryEditForm

@login_required
@permission_required('story.view_story')
def list_stories(request):
    stories = Story.objects.order_by('title')
    return render(request, 'planner/story/story_table.html', {'stories': stories})

@login_required
@permission_required('story.view_story')
def get_table(request):
    stories = Story.objects.order_by('title')
    return render(request, 'planner/story/table_rows.html', {'stories': stories})

@login_required
@permission_required('story.view_story')
def view_story(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    return render(request, 'planner/story/detailed.html', {'story': story})

class StoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'story.add_story'

    def get(self, request, epic_id=None):
        epics = [(t.id, t.title) for t in Epic.objects.all()]
        initial_epics = [epic_id]
        form = StoryEditForm(initial={'epics': initial_epics}, epics=epics)
        return render(request, 'planner/story/quick_edit_form.html', {'form': form})

    def post(self, request):
        epics = [(t.id, t.title) for t in Epic.objects.all()]
        form = StoryEditForm(request.POST, epics=epics)
        if form.is_valid():
            story = Story()
            story.title = form.cleaned_data['title']
            story.save()
            for epic_id in form.cleaned_data['epics']:
                story.epic_set.add(epic_id)
            response = render(request, 'common/close_modal.html')
            trigger_events = ['reloadAllEpics']
            for epic in form.cleaned_data['epics']:
                trigger_events.append(f'reloadStories-{epic}')
            response['HX-Trigger'] = ", ".join(trigger_events)
        else:
            response = render(request, 'planner/story/quick_edit_form.html', {'form': form})
        return response

class StoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'story.change_story'

    def get(self, request, story_id):
        story = get_object_or_404(Story, pk=story_id)
        epics = [(t.id, t.title) for t in Epic.objects.all()]
        initial_epics = [t.id for t in story.epic_set.all()]
        form = StoryEditForm(initial={'title': story.title, 'epics': initial_epics}, epics=epics)
        return render(request, 'planner/story/quick_edit_form.html', {'form': form, 'story': story})

    def post(self, request, story_id):
        story = get_object_or_404(Story, pk=story_id)
        epics = [(t.id, t.title) for t in Epic.objects.all()]
        form = StoryEditForm(request.POST, epics=epics)
        if form.is_valid():
            story.title = form.cleaned_data['title']
            story.epic_set.clear()
            for epic_id in form.cleaned_data['epics']:
                story.epic_set.add(epic_id)
            story.save()
            response = render(request, 'common/close_modal.html')
            response['HX-Trigger'] = 'newStory'
            return response
        return render(request, 'planner/story/quick_edit_form.html', {'form': form, 'story': story})

class StoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'story.delete_story'

    def delete(self, request, story_id):
        Story.objects.filter(pk=story_id).delete()
        return HttpResponse(status=200)
