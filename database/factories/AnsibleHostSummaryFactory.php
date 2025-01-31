<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\ansibleHost_summary>
 */
class AnsibleHostSummaryFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'hostname' => Str::random(16),
            'os_version' => Str::random(16),
            'python3_version' => Str::random(16),
            'status_notes' => Str::random(16),
            'virtual_disk_size' => fake()->randomNumber(3),
            'special_notes' => Str::random(48),
            'running' => fake()->boolean(),
            'cyteen_vm_cpu_allocation' => fake()->randomNumber(1),
            'cyteen_vm_ram_allocation' => fake()->randomNumber(4),
            'r720_vm_cpu_allocation' => fake()->randomNumber(1),
            'r720_vm_ram_allocation' => fake()->randomNumber(4),
        ];
    }
}
