from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Index")


def login(request):
    """
    Handles login actions (display login form, handle passed data)
    :param request: incoming request
    :type request: HttpRequest
    :return: response
    :rtype: HttpResponse
    """
    return render(request, 'login.html')
