<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class AnsibleHostSummary extends Model
{
    /** @use HasFactory<\Database\Factories\AnsibleHostSummaryFactory> */
    use HasFactory;

    protected $fillable = [
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
    ];

    protected $table = 'ansible_host_summary';

    public $timestamps = false;
}
