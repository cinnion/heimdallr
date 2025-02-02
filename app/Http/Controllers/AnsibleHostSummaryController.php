<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class AnsibleHostSummary extends Controller
{
    public function index(Request $request)
    {
        if ($request->ajax()) {
            $ansible_host_summary = \App\Models\AnsibleHostSummary::query();;

            dd($ansible_host_summary);
        } else {
            return view('ansible-host-summary');
        }
    }
}
