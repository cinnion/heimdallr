from django.db import models

class AnsibleHostSummary(models.Model):
    hostname = models.CharField(max_length=32, unique=True)
    os_version = models.CharField(max_length=32, null=True)
    python3_version = models.CharField(max_length=32, null=True)
    status_notes = models.CharField(max_length=256, null=True)
    virtual_disk_size_mb = models.IntegerField(null=True)
    special_notes = models.CharField(max_length=64, null=True)
    running = models.BooleanField(default=False, null=True)
    cyteen_vm_cpu_allocation = models.IntegerField(null=True)
    cyteen_vm_ram_allocation = models.IntegerField(null=True)
    r720_vm_cpu_allocation = models.IntegerField(null=True)
    r720_vm_ram_allocation = models.IntegerField(null=True)

    class Meta:
        db_table = 'ansible_host_summary'

    def cyteen_vm_cpu_use(self):
        if self.running and self.cyteen_vm_cpu_allocation:
            usage = self.cyteen_vm_cpu_allocation
        else:
            usage = None

        return usage

    def cyteen_vm_ram_use(self):
        if self.running and self.cyteen_vm_ram_allocation:
            usage = self.cyteen_vm_ram_allocation
        else:
            usage = None

        return usage

    def r720_vm_cpu_use(self):
        if self.running and self.r720_vm_cpu_allocation:
            usage = self.r720_vm_cpu_allocation
        else:
            usage = None

        return usage

    def r720_vm_ram_use(self):
        if self.running and self.r720_vm_ram_allocation:
            usage = self.r720_vm_ram_allocation
        else:
            usage = None

        return usage
