
from django.urls import path
from django.conf.urls import include

from .views import dashboard, get_dashboard_themes, get_dashboard_epics

app_name = 'agile'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('get-dashboard-themes', get_dashboard_themes, name='get-dashboard-themes'),
    path('get-dashboard-epics/<int:theme_id>', get_dashboard_epics, name='get-dashboard-epics'),
    path('theme/', include('apps.agile.theme.urls')),
    path('epic/', include('apps.agile.epic.urls')),
    path('story/', include('apps.agile.story.urls')),
]
