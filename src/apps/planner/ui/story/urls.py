from django.urls import path

from .views import list_stories, get_table, view_story, StoryUpdateView, StoryDeleteView, StoryCreateView

app_name = 'story'

urlpatterns = [
    path('', list_stories, name='list'),
    path('table', get_table, name='get-table'),
    path('<int:story_id>', view_story, name='view'),
    path('add', StoryCreateView.as_view(), name='add'),
    path('add/<int:epic_id>', StoryCreateView.as_view(), name='add'),
    path('<int:story_id>/delete', StoryDeleteView.as_view(), name='delete'),
    path('<int:story_id>/edit', StoryUpdateView.as_view(), name='edit'),
]
