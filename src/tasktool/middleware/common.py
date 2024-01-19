from django.utils import translation

from apps.account.models import AccountSettings


class CancelLinkMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.prefixes_filtered = (
            '/ajax',
            '/jsi18n',
            '/media',
            '/static',
            '/i18n',
            '/admin',
        )
        self.suffixes_filtered = (
            'update',
            'update/',
            'delete',
            'delete/',
            'create',
            'create/',
        )

    def __call__(self, request):
        if 'cancel_link' not in request.session:
            request.session['cancel_link'] = '/'
            request.session.modified = True

        if request.path.startswith(self.prefixes_filtered):
            return self.get_response(request)

        if request.path.endswith(self.suffixes_filtered):
            return self.get_response(request)

        request.session['cancel_link'] = request.path
        request.session.modified = True

        return self.get_response(request)


class LanguageSelectionMiddleware:
    """Site language is specified by a setting under user profile.
    This middleware is also used to ensure that the user-specific settings
    exist for every user.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        user_settings, _ = AccountSettings.objects.get_or_create(
            user_id=request.user.id)
        translation.activate(user_settings.selected_lang)

        return self.get_response(request)
