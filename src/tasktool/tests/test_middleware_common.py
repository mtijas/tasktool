from django.test import TestCase
from tasktool.middleware.common import CancelLinkMiddleware
from unittest.mock import MagicMock


class CancelLinkTestCase(TestCase):
    def test_path_starting_with_ajax_does_not_set_link(self):
        """When path starts with '/ajax', cancel link should not be set"""
        get_response = MagicMock()
        request = MagicMock()
        request.path = '/ajax/path/to/somewhere/'

        middleware = CancelLinkMiddleware(get_response=get_response)
        middleware(request)

        request.session.__setitem__.assert_called_with('cancel_link', '/')

    def test_path_ending_in_update_does_not_set_link(self):
        """When path ends with 'update', cancel link should not be set"""
        get_response = MagicMock()
        request = MagicMock()
        request.path = '/path/to/somewhere/update'

        middleware = CancelLinkMiddleware(get_response=get_response)
        middleware(request)

        request.session.__setitem__.assert_called_with('cancel_link', '/')

    def test_path_ending_in_update_does_not_set_link_test_2(self):
        """When path ends with 'update/', cancel link should not be set"""
        get_response = MagicMock()
        request = MagicMock()
        request.path = '/path/to/somewhere/update/'

        middleware = CancelLinkMiddleware(get_response=get_response)
        middleware(request)

        request.session.__setitem__.assert_called_with('cancel_link', '/')

    def test_path_ending_in_create_does_not_set_link(self):
        """When path ends with 'create', cancel link should not be set"""
        get_response = MagicMock()
        request = MagicMock()
        request.path = '/path/to/somewhere/create'

        middleware = CancelLinkMiddleware(get_response=get_response)
        middleware(request)

        request.session.__setitem__.assert_called_with('cancel_link', '/')

    def test_path_ending_in_create_does_not_set_link_test_2(self):
        """When path ends with 'create/', cancel link should not be set"""
        get_response = MagicMock()
        request = MagicMock()
        request.path = '/path/to/somewhere/create/'

        middleware = CancelLinkMiddleware(get_response=get_response)
        middleware(request)

        request.session.__setitem__.assert_called_with('cancel_link', '/')

    def test_path_ending_in_delete_does_not_set_link(self):
        """When path ends with 'delete', cancel link should not be set"""
        get_response = MagicMock()
        request = MagicMock()
        request.path = '/path/to/somewhere/delete'

        middleware = CancelLinkMiddleware(get_response=get_response)
        middleware(request)

        request.session.__setitem__.assert_called_with('cancel_link', '/')

    def test_path_ending_in_delete_does_not_set_link_test_2(self):
        """When path ends with 'delete/', cancel link should not be set"""
        get_response = MagicMock()
        request = MagicMock()
        request.path = '/path/to/somewhere/delete/'

        middleware = CancelLinkMiddleware(get_response=get_response)
        middleware(request)

        request.session.__setitem__.assert_called_with('cancel_link', '/')

    def test_path_get_passed_to_cancel_link(self):
        """Path should get passed to cancel link by default"""
        get_response = MagicMock()
        request = MagicMock()
        request.path = '/path/to/somewhere/'

        middleware = CancelLinkMiddleware(get_response=get_response)
        middleware(request)

        request.session.__setitem__.assert_called_with('cancel_link', request.path)

    def test_slash_path(self):
        """Slash path should get passed to cancel link"""
        get_response = MagicMock()
        request = MagicMock()
        request.path = '/'

        middleware = CancelLinkMiddleware(get_response=get_response)
        middleware(request)

        request.session.__setitem__.assert_called_with('cancel_link', request.path)

    def test_empty_path(self):
        """Empty path should get passed to cancel link"""
        get_response = MagicMock()
        request = MagicMock()
        request.path = ''

        middleware = CancelLinkMiddleware(get_response=get_response)
        middleware(request)

        request.session.__setitem__.assert_called_with('cancel_link', request.path)
