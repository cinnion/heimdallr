<?php

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('home');
});

Route::get('/ansible-host-summary', [\App\Http\Controllers\AnsibleHostSummaryController::class, 'index'])
    ->name('ansible-host-summary');

Route::get('/firewall', [\App\Http\Controllers\FirewallController::class, 'index'])
    ->name('firewall.index');
Route::get('/firewall/blackholes', [\App\Http\Controllers\FirewallBlackholeController::class, 'summary'])
    ->name('firewall.blackholes');
Route::get('/firewall/heavy-hitters', [\App\Http\Controllers\FirewallHeavyHittersController::class, 'summary'])
    ->name('firewall.heavy-hitters');

