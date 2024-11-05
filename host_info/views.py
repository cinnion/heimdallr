from django.http import HttpResponse
from django.template import loader

from host_info.models import AnsibleHostSummary


def ansible_host_summary(request):
    hosts = AnsibleHostSummary.objects.order_by('hostname').all()

    cyteen_vm_cpu_total = 0
    cyteen_vm_ram_total = 0
    r720_vm_cpu_total = 0
    r720_vm_ram_total = 0

    for host in hosts:
        cyteen_vm_cpu_total += host.cyteen_vm_cpu_use or 0
        cyteen_vm_ram_total += host.cyteen_vm_ram_use or 0
        r720_vm_cpu_total   += host.r720_vm_cpu_use or 0
        r720_vm_ram_total   += host.r720_vm_ram_use or 0

    totals = {
        "cyteen_vm_cpu_total": cyteen_vm_cpu_total,
        "cyteen_vm_ram_total": cyteen_vm_ram_total,
        "r720_vm_cpu_total": r720_vm_cpu_total,
        "r720_vm_ram_total": r720_vm_ram_total,
    }

    context = {
        'host_summary': hosts,
        'totals': totals,
    }

    template = loader.get_template('AnsibleHostSummary.html')
    return HttpResponse(template.render(context, request))

