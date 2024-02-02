from django.db import models
from django.utils.translation import gettext_lazy as _

from .epic import Epic


class Theme(models.Model):
    title = models.TextField(
        verbose_name=_('title')
    )
    description = models.TextField(
        verbose_name=_('description'),
        blank=True
    )
    epics = models.ManyToManyField(Epic)


    class Meta():
        ordering = ['title']
        verbose_name = _('theme')
        verbose_name_plural = _('themes')

    def __str__(self):
        return self.title
