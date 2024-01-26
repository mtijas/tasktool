from django.urls import path

from . import views
from .views import TagUpdateView, TagDeleteView, TagCreateView

app_name = 'tag'

urlpatterns = [
    path('', views.list_tags, name='list'),
    path('table', views.get_table, name='get-table'),
    path('add', TagCreateView.as_view(), name='add'),
    path('<int:tag_id>/delete', TagDeleteView.as_view(), name='delete'),
    path('<int:tag_id>/edit', TagUpdateView.as_view(), name='edit'),
]
