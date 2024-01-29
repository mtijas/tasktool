from django.db import models
from django.utils.translation import gettext_lazy as _

from ..theme.models import Theme


class Epic(models.Model):
    title = models.TextField(
        verbose_name=_('title')
    )
    description = models.TextField(
        verbose_name=_('description'),
        blank=True
    )
    themes = models.ManyToManyField(Theme)


    class Meta():
        ordering = ['title']
        verbose_name = _('epic')
        verbose_name_plural = _('epics')

    def __str__(self):
        return self.title
