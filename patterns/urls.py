from django.urls import path, re_path
from .views import index, create, details, edit, delete


urlpatterns = [
    re_path(r'^(?P<user_id>[0-9]+)$', index),
    re_path(r'^index/(?P<user_id>[0-9]+)$', index),
    path('create', create),
    re_path(r'^details/(?P<pattern_id>[0-9]+)$', details),
    re_path(r'^edit/(?P<pattern_id>[0-9]+)$', edit),
    re_path(r'^delete/(?P<pattern_id>[0-9]+)$', delete)
]
