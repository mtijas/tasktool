from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    title = models.TextField(
        verbose_name=_('title')
    )
    description = models.TextField(
        verbose_name=_('description')
    )
    

    class Meta():
        ordering = ['id']
        verbose_name = _('task')
        verbose_name_plural = _('tasks')

    def __str__(self):
        return self.title
