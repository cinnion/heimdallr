from django.db import models

class AnsibleHostSummary(models.Model):
    hostname = models.CharField(max_length=32, unique=True)
    os_version = models.CharField(max_length=32, blank=True, null=True)
    python3_version = models.CharField(max_length=32, blank=True, null=True)
    status_notes = models.CharField(max_length=256, blank=True, null=True)
    virtual_disk_size_mb = models.IntegerField(blank=True, null=True)
    special_notes = models.CharField(max_length=64, blank=True, null=True)
    running = models.BooleanField(default=False, blank=True, null=True)
    cyteen_vm_cpu_allocation = models.IntegerField(blank=True, null=True)
    cyteen_vm_ram_allocation = models.IntegerField(blank=True, null=True)
    r720_vm_cpu_allocation = models.IntegerField(blank=True, null=True)
    r720_vm_ram_allocation = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ansible_host_summary'

    @property
    def cyteen_vm_cpu_use(self):
        if self.running and self.cyteen_vm_cpu_allocation:
            usage = self.cyteen_vm_cpu_allocation
        else:
            usage = None

        return usage

    @property
    def cyteen_vm_ram_use(self):
        if self.running and self.cyteen_vm_ram_allocation:
            usage = self.cyteen_vm_ram_allocation
        else:
            usage = None

        return usage

    @property
    def r720_vm_cpu_use(self):
        if self.running and self.r720_vm_cpu_allocation:
            usage = self.r720_vm_cpu_allocation
        else:
            usage = None

        return usage

    @property
    def r720_vm_ram_use(self):
        if self.running and self.r720_vm_ram_allocation:
            usage = self.r720_vm_ram_allocation
        else:
            usage = None

        return usage
