from django.urls import path
from .views import index, number_rows, number_stitches, rapport


urlpatterns = [
    path('', index),
    path('index', index),
    path('rows', number_rows),
    path('stitches', number_stitches),
    path('rapport', rapport)
]