from django.urls import path

from .views import dashboard, get_dashboard_themes, get_dashboard_epics, get_dashboard_stories

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('get-dashboard-themes', get_dashboard_themes, name='get-dashboard-themes'),
    path('get-dashboard-epics/<int:theme_id>', get_dashboard_epics, name='get-dashboard-epics'),
    path('get-dashboard-stories/<int:epic_id>', get_dashboard_stories, name='get-dashboard-stories'),
]
