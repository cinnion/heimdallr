from typing import List, Union

from django.urls import path, URLResolver, URLPattern
from . import views

urlpatterns: List[Union[URLResolver, URLPattern]] = [
    path('host_info/', views.ansible_host_summary, name='AnsibleHostSummary')
]
