from django.urls import path

from . import views
from .views import TaskView

app_name = 'task'

urlpatterns = [
    path('', views.list_tasks, name='list'),
    path('add', views.add_task, name='add'),
    path('table', views.get_table, name='get-table'),
    path('<int:task_id>', TaskView.as_view(), name='delete'),
]
