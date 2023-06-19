# coding: utf-8

try:
    from django.urls.defaults import path
except ImportError:
    from django.urls import path

from . import views as v


urlpatterns = [
    path(r'^result/$', v.receive_result, name='robokassa_result'),
    path(r'^success/$', v.success, name='robokassa_success'),
    path(r'^fail/$', v.fail, name='robokassa_fail'),
]
