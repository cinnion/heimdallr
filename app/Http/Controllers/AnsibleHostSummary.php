<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class AnsibleHostSummary extends Controller
{
    public function summary()
    {
        return view('ansible-host-summary');
    }
}
