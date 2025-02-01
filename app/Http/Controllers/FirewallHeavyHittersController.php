<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class FirewallHeavyHittersController extends Controller
{
    public function summary()
    {
        return view('firewall.heavy-hitter-summary');
    }
}
