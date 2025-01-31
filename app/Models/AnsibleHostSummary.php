<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class AnsibleHostSummary extends Model
{
    /** @use HasFactory<\Database\Factories\AnsibleHostSummaryFactory> */
    use HasFactory;

    protected $table = 'ansible_host_summary';

    public $timestamps = false;
}
