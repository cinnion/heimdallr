<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class FirewallBlackholeController extends Controller
{
    public function summary()
    {
        return view('firewall.blackhole-summary');
    }
}
