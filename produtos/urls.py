
from django.urls import include, path
from .views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),
]


