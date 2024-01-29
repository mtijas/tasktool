from django.urls import path

from .views import list_epics, get_table, EpicUpdateView, EpicDeleteView, EpicCreateView

app_name = 'epic'

urlpatterns = [
    path('', list_epics, name='list'),
    path('table', get_table, name='get-table'),
    path('add', EpicCreateView.as_view(), name='add'),
    path('add/<int:theme_id>', EpicCreateView.as_view(), name='add'),
    path('<int:epic_id>/delete', EpicDeleteView.as_view(), name='delete'),
    path('<int:epic_id>/edit', EpicUpdateView.as_view(), name='edit'),
]
