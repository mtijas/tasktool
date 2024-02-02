
from django.urls import path
from django.conf.urls import include

app_name = 'planner'

urlpatterns = [
    path('', include('apps.planner.ui.dashboard.urls')),
    path('theme/', include('apps.planner.ui.theme.urls')),
    path('epic/', include('apps.planner.ui.epic.urls')),
    path('story/', include('apps.planner.ui.story.urls')),
]
