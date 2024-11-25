from django.shortcuts import render, redirect, get_object_or_404

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

def host_details(request, hostid=None):

    if hostid:
        host = get_object_or_404(AnsibleHostSummary, pk=hostid)
    else:
        host = AnsibleHostSummary()

    form = forms.EditHost(request.POST or None, instance=host)

    if request.method == 'POST'and form.is_valid():
        form.save()
        return redirect('host_info:host-summary')

    return render(request, 'HostDetailsForm.html', {'form': form})

def host_new(request):
    if request.method == 'POST':
        form = forms.CreateHost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('host_info:host-summary')
    else:
        form = forms.CreateHost()
    return render(request, 'NewHostForm.html', { 'form': form})

