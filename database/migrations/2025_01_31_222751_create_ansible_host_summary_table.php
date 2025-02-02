<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('ansible_host_summary', function (Blueprint $table) {
            $table->id();
            $table->string('hostname', 32)->unique();
            $table->string('os_version', 32)->nullable();
            $table->string('python3_version', 32)->nullable();
            $table->string('status_notes', 256)->nullable();
            $table->integer('virtual_disk_size_mb')->nullable();
            $table->string('special_notes', 64)->nullable();
            $table->boolean('running')->default(false)->nullable();
            $table->integer('cyteen_vm_cpu_allocation')->nullable();
            $table->integer('cyteen_vm_ram_allocation')->nullable();
            $table->integer('r720_vm_cpu_allocation')->nullable();
            $table->integer('r720_vm_ram_allocation')->nullable();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('ansible_host_summary');
    }
};
