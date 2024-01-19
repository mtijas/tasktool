from datetime import datetime, timedelta
from unittest.mock import Mock

from django.test import TestCase

from tasktool.templatetags import tasktool_extras


class TemplateTagsTestCase(TestCase):
    def test_active_returns_str_active_simple_path(self):
        """Active should return string 'active' when first element of path matches"""
        request = Mock()
        request.path = '/exists/'
        target = 'exists'

        result = tasktool_extras.active(request, target)

        self.assertEquals(result, 'active')

    def test_active_returns_str_active_complex_path(self):
        """Active should return string 'active' when first element of path matches"""
        request = Mock()
        request.path = '/exists/in/more/complex/path/'
        target = 'exists'

        result = tasktool_extras.active(request, target)

        self.assertEquals(result, 'active')

    def test_active_returns_empty_str_when_target_not_first_element(self):
        """Active should return string 'active' when first element of path matches"""
        request = Mock()
        request.path = '/not/exists/'
        target = 'exists'

        result = tasktool_extras.active(request, target)

        self.assertEquals(result, '')
