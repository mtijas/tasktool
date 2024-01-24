from django.urls import path

from . import views
from .views import TaskModifyView, TaskCreateView

app_name = 'task'

urlpatterns = [
    path('', views.list_tasks, name='list'),
    path('table', views.get_table, name='get-table'),
    path('add', TaskCreateView.as_view(), name='add'),
    path('<int:task_id>', TaskModifyView.as_view(), name='delete'),
    path('<int:task_id>', TaskModifyView.as_view(), name='edit'),
]
