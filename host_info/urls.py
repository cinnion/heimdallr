from typing import List, Union

from django.urls import path, URLResolver, URLPattern
from . import views

app_name='host_details'

urlpatterns: List[Union[URLResolver, URLPattern]] = [
    path('', views.ansible_host_summary, name='host-summary'),
    path('<int:hostid>', views.host_details, name='host-details'),
    path('new-host/', views.host_new, name='new-host'),
]
