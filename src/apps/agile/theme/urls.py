from django.urls import path

from .views import list_themes, get_table, ThemeUpdateView, ThemeDeleteView, ThemeCreateView

app_name = 'theme'

urlpatterns = [
    path('', list_themes, name='list'),
    path('table', get_table, name='get-table'),
    path('add', ThemeCreateView.as_view(), name='add'),
    path('<int:theme_id>/delete', ThemeDeleteView.as_view(), name='delete'),
    path('<int:theme_id>/edit', ThemeUpdateView.as_view(), name='edit'),
]
