from django.urls import path
from toster.views import index, test

urlpatterns = [
    path('', index, name='index'),
    path('test', test, name='test'),
]
