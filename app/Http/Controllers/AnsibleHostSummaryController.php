<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\AnsibleHostSummary;
use Yajra\DataTables\Facades\DataTables;

class AnsibleHostSummaryController extends Controller
{
    public function index(Request $request)
    {
        if ($request->ajax()) {
            $ansible_host_summary = AnsibleHostSummary::query();

            return DataTables::eloquent($ansible_host_summary)->make(true);
        } else {
            return view('ansible-host-summary');
        }
    }
}
