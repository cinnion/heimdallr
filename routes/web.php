<?php

use App\Http\Controllers\ProfileController;
use App\Http\Controllers\AnsibleHostSummaryController;
use App\Http\Controllers\FirewallHeavyHittersController;
use App\Http\Controllers\FirewallBlackholeController;
use App\Http\Controllers\FirewallController;
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('home');
});

Route::get('/dashboard', function () {
    return view('dashboard');
})->middleware(['auth', 'verified'])->name('dashboard');

Route::middleware('auth')->group(function () {
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
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

require __DIR__.'/auth.php';
