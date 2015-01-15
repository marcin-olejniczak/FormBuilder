from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^formbuilder/',
        include('formbuilder.urls', namespace="formbuilder")),
    url(r'',
        include('formbuilder.urls', namespace="formbuilder")),
    url(r'^admin/', include(admin.site.urls)),
)
