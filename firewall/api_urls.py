from typing import List, Union
from django.urls import path, URLResolver, URLPattern
from . import views


urlpatterns: List[Union[URLResolver, URLPattern]] = [
    path('blackholes', views.Blackholes.as_view()),
    path('heavyHitters', views.HeavyHitters.as_view()),
]
