from django.urls import path

from .views import BaseDashboardView

urlpatterns = [
    path('', BaseDashboardView.as_view(), name='base-dashboard'),
]