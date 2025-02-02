<?php

use Illuminate\Support\Facades\Route;
use \App\Http\Controllers\AnsibleHostSummaryController;
use App\Http\Controllers\FirewallHeavyHittersController;
use App\Http\Controllers\FirewallBlackholeController;
use App\Http\Controllers\FirewallController;

Route::get('/', function () {
    return view('home');
});

Route::get('/firewall', [FirewallController::class, 'index'])
    ->name('firewall.index');

Route::resources([
    'ansible-host-summary' => AnsibleHostSummaryController::class,
    'blackholes' => FirewallBlackholeController::class
]);

Route::get('blackholes/{cidrBlock}/add', [FirewallBlackholeController::class, 'add'])
    ->name('blackholes.add');
Route::get('/firewall/heavy-hitters', [FirewallHeavyHittersController::class, 'index'])
    ->name('heavyhitters.index');
Route::get('/firewall/heavyhitters/{cidrBlock}/detail', [FirewallHeavyHittersController::class, 'details'])
    ->name('heavyhitters.detail');
