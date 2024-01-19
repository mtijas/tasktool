from django.urls import path

from .views import BasicAccountsView, AccountSettingsEditView

urlpatterns = [
    path('', BasicAccountsView.as_view(), name='account'),
    path('update', AccountSettingsEditView.as_view(), name='accountsettingsedit'),
]
