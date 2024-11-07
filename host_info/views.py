from django.shortcuts import render, redirect

from host_info.models import AnsibleHostSummary
from . import forms


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

    return render(request, 'AnsibleHostSummary.html', context)

def host_details(request, hostid):

    form = forms.EditHost
    host = AnsibleHostSummary.objects.get(pk=hostid)

    return render(request, 'HostDetailsForm.html', {"host": host, 'form': form})

def host_new(request):
    if request.method == 'POST':
        form = forms.CreateHost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('host_info:host-summary')
    else:
        form = forms.CreateHost()
    return render(request, 'NewHostForm.html', { 'form': form})

