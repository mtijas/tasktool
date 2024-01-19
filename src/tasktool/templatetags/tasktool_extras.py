from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag
def active(request, pattern):
    import re

    if re.search(f'^\/{pattern}', request.path):
        return 'active'
    return ''