from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    title = models.TextField(
        verbose_name=_('title')
    )
    background_color = models.CharField(
        max_length=32,
        blank=True,
        validators=[
            RegexValidator(r'^#(?:[0-9a-fA-F]{3}){1,2}$'),
        ],
        verbose_name=_("background colour")
    )
    text_color = models.CharField(
        max_length=32,
        blank=True,
        validators=[
            RegexValidator(r'^#(?:[0-9a-fA-F]{3}){1,2}$'),
        ],
        verbose_name=_("text colour")
    )


    class Meta():
        ordering = ['title']
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.title
