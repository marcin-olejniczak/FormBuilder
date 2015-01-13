from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from snaplib.api2.api import Api
from .view_decorators import (require_authentication,)


@require_authentication
def index(request):
    return HttpResponse("Zalogowany")


def login(request):
    """
    Handles login actions (display login form, handle passed data)
    :param request: incoming request
    :type request: HttpRequest
    :return: response
    :rtype: HttpResponse
    """
    request.session.flush()
    if request.POST:
        api = Api(settings.SNAP_API_BASE_URL, settings.SNAP_INITIAL_PRINCIPAL)
        response = api.authenticate(
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if response.status_code >= 400:
            return render(
                request,
                'login.html',
                {'error_message': response.json()['message']}
            )
        request.session['user'] = response.json()['user']
        request.session['profile'] = response.json()['userProfile']
        # request.session['api'] = api
        return HttpResponseRedirect(reverse('formbuilder:index'))

    return render(request, 'login.html')
