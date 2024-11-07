from django import forms
from . import models

class CreateHost(forms.ModelForm):
    class Meta:
        model = models.AnsibleHostSummary
        fields = [ 'hostname',
                   'os_version',
                   'python3_version',
                   'status_notes',
                   'virtual_disk_size_mb',
                   'special_notes',
                   'running',
                   'cyteen_vm_cpu_allocation',
                   'cyteen_vm_ram_allocation',
                   'r720_vm_cpu_allocation',
                   'r720_vm_ram_allocation',
                   ]

class EditHost(forms.ModelForm):
    class Meta:
        model = models.AnsibleHostSummary
        fields = ['id',
                  'hostname',
                  'os_version',
                  'python3_version',
                  'status_notes',
                  'virtual_disk_size_mb',
                  'special_notes',
                  'running',
                  'cyteen_vm_cpu_allocation',
                  'cyteen_vm_ram_allocation',
                  'r720_vm_cpu_allocation',
                  'r720_vm_ram_allocation',
                  ]