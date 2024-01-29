from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag
def active(request, pattern, complete_match=False):
    import re

    search_str = f'^\/{pattern}'

    if complete_match:
        search_str += '\/$'

    if re.search(search_str, request.path):
        return 'active'
    return ''
