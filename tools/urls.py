from django.urls import re_path
from .views import index, create, edit, delete


urlpatterns = [
    re_path(r'^(?P<user_id>[0-9]+)$', index),
    re_path(r'^index/(?P<user_id>[0-9]+)$', index),
    re_path(r'create', create),
    re_path(r'^edit/(?P<tool_id>[0-9]+)$', edit),
    re_path(r'^delete/(?P<tool_id>[0-9]+)$', delete)
]
