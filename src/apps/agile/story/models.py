from django.db import models
from django.utils.translation import gettext_lazy as _


class Story(models.Model):
    title = models.TextField(
        verbose_name=_('title')
    )


    class Meta():
        ordering = ['title']
        verbose_name = _('story')
        verbose_name_plural = _('stories')

    def __str__(self):
        return self.title
