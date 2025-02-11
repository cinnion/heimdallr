<?php

namespace App\Http\Controllers;

use App\Models\Blacklist;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Gate;
use Yajra\DataTables\Facades\DataTables;

class FirewallBlackholeController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index(Request $request)
    {
        if ($request->ajax()) {
            $blackholes = Blacklist::query();

            return DataTables::eloquent($blackholes)
                ->AddIndexColumn()
                ->addColumn('action', function ($blackhole) {
                    $retval = '<a href="' . route('heavyhitters.detail', $blackhole) . '" class="btn btn-success btn-sm" target="_blank">Details</a>';

                    return $retval;
                })
                ->rawColumns(['action'])
                ->make(true);
        } else {
            return view('firewall.blackholes');
        }
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        Gate::authorize('admin');

        $cidrBlock = $request->post('blackhole');
        $cidrBlock = str_replace('-', '/', $cidrBlock);

        $rec = new Blacklist(['blackhole' => $cidrBlock]);
        try {
            $rec->save();
            return response()->json(['status' => 'success', 'message' => 'Blackhole added successfully']);
        } catch (Exception $e) {
            return response()->json([ 'status' => 'failed', 'message' => 'Unable to add blackhole ' . $cidrBlock]);

        }
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
    }
}
