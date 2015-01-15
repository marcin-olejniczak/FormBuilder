from django.conf.urls import patterns, url

from formbuilder import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^builder$', views.builder, name='builder'),
    url(r'^get_form_templates$', views.get_form_templates,
        name='get_form_templates'),
)
