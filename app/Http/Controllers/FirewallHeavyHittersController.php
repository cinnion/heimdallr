<?php

namespace App\Http\Controllers;

use App\Models\HeavyHitter;
use Illuminate\Http\Request;
use Yajra\DataTables\Facades\DataTables;

class FirewallHeavyHittersController extends Controller
{
    public function index(Request $request)
    {
        if ($request->ajax()) {
            $heavy_hitters = HeavyHitter::query();

            return DataTables::eloquent($heavy_hitters)->make(true);
        } else {
            return view('firewall.heavy-hitters');
        }
    }
}
