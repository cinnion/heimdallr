from typing import List, Union
from django.urls import path, URLResolver, URLPattern
from . import views

app_name = 'firewall'

urlpatterns: List[Union[URLResolver, URLPattern]] = [
    path('', views.menu, name='firewall-menu'),
    path('blackholes', views.blackholes, name='blackholes'),
    path('heavyHitters', views.HeavyHitters.as_view()),
    path('heavyHittersList', views.heavy_hitters_list, name='heavy-hitters-list'),

]
