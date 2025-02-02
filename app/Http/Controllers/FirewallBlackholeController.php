<?php

namespace App\Http\Controllers;

use App\Models\Blacklist;
use Illuminate\Http\Request;
use Yajra\DataTables\Facades\DataTables;

class FirewallBlackholeController extends Controller
{
    public function index(Request $request)
    {
        if ($request->ajax()) {
            $blackholes = Blacklist::query();

            return DataTables::eloquent($blackholes)->make(true);
        } else {
            return view('firewall.blackholes');
        }
    }
}
