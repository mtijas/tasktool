from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, reverse
from django.utils.translation import gettext
from django.views.generic import TemplateView, View

from .forms import AccountSettingsForm
from .models import AccountSettings


class BasicAccountsView(LoginRequiredMixin, TemplateView):
    """Accounts view"""

    template_name = "accounts/accounts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        (accountsettings, _) = AccountSettings.objects.get_or_create(
            user_id=self.request.user.id, defaults={"user": self.request.user})

        context["accounts_list"] = User.objects.all()
        context["accountsettings"] = accountsettings
        context["user_permissions"] = self.request.user.get_all_permissions()
        return context


class AccountSettingsEditView(LoginRequiredMixin, View):

    template_name = "accountsettings/edit.html"

    def get(self, request, *args, **kwargs):
        settings = AccountSettings.objects.filter(user_id=request.user.id).first()
        form = AccountSettingsForm(instance=settings)

        data = {
            "form": form,
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        settings = AccountSettings.objects.filter(user_id=request.user.id).first()
        form = AccountSettingsForm(request.POST, instance=settings)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                gettext("Settings edited successfully.")
            )
            return redirect(reverse("profile"))

        data = {
            "form": form,
        }
        return render(request, self.template_name, data)
