import json
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from snaplib.api2.api import Api
from .view_decorators import (require_authentication,)


@require_authentication
def index(request):
    """
    Display catalog with available forms
    :param request: incoming request
    :type request: HttpRequest
    :return: response
    :rtype: HttpResponse
    """
    return render(request, 'catalog.html')


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


@require_authentication
def get_form_templates(request):
    """
    returns json with templates
    :param request: incoming request
    :type request: HttpRequest
    :return: response
    :rtype: HttpResponse
    """
    api = Api(settings.SNAP_API_BASE_URL, settings.SNAP_INITIAL_PRINCIPAL)
    templates_collection = api['/formTemplates']
    templates = []
    for template in list(templates_collection.collection_items()):
        t = {
            'name': template['formTemplate']['data']['name'],
            'revisionNumber': template[
                'formTemplate']['data']['revisionNumber'],
            'status': template['formTemplate']['data']['status'],
            'uuid': template['formTemplate']['metadata']['uuid']
        }
        templates.insert(0, t)
    return HttpResponse(json.dumps(templates))


@require_authentication
def builder(request):
    """
    Display form Builder 
    :param request: incoming request
    :type request: HttpRequest
    :return: response
    :rtype: HttpResponse
    """
    return render(request, 'builder.html')
