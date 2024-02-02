from django.db import models
from django.utils.translation import gettext_lazy as _

from .story import Story


class Epic(models.Model):
    title = models.TextField(
        verbose_name=_('title')
    )
    description = models.TextField(
        verbose_name=_('description'),
        blank=True
    )
    stories = models.ManyToManyField(Story)


    class Meta():
        ordering = ['title']
        verbose_name = _('epic')
        verbose_name_plural = _('epics')

    def __str__(self):
        return self.title
