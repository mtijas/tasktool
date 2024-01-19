from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class AccountSettings(models.Model):

    selected_lang = models.CharField(
        max_length=5,
        default="en",
        choices=settings.LANGUAGES,
        verbose_name=_("selected language")
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("user")
    )
