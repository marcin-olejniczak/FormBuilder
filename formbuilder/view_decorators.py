from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def require_authentication(view):
    def temp_function(request):
        if 'user' in request.session:
            return view(request)
        else:
            return HttpResponseRedirect(reverse('formbuilder:login'))
    return temp_function
