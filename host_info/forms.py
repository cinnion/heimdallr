from django.forms import CharField, ModelForm

from . import models

class CreateHost(ModelForm):
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

class EditHost(ModelForm):
    os_version = CharField(
        max_length=32,
        label="OS Version",
        required=False,
        help_text='OS Version (e.g. "Rocky 9.4")'
    )

    class Meta:
        model = models.AnsibleHostSummary
        exclude = ['id']
