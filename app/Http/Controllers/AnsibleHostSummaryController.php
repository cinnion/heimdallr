<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\AnsibleHostSummary;
use Yajra\DataTables\Facades\DataTables;

class AnsibleHostSummaryController extends Controller
{
    /**
     * Display a listing of the host summaries.
     *
     * @param Request $request
     * @return \Illuminate\Contracts\View\Factory|\Illuminate\Contracts\View\View|\Illuminate\Foundation\Application|\Illuminate\Http\JsonResponse
     * @throws \Exception
     */
    public function index(Request $request)
    {
        if ($request->ajax()) {
            $ansible_host_summary = AnsibleHostSummary::query();

            return DataTables::eloquent($ansible_host_summary)
                ->addColumn('action', function ($host) {
                    $retval = '<a href="' . route('ansible-host-summary.show', $host->id) . '" class="btn btn-success btn-sm" target="_blank">Details</a>';
                    $retval .= '&nbsp;<button value="' . $host->id . '" class="btn btn-danger btn-sm delete-host">Delete</button>';

                    return $retval;
                })
                ->rawColumns(['action'])
                ->make(true);
        } else {
            return view('ansible-host-summary');
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
        //
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
        $host = AnsibleHostSummary::findOrFail($id);
        if ($host) {
            $host->delete();
            return response()->json(['status' => 'success', 'message' => 'Host deleted successfully']);
        }
        return response()->json([ 'status' => 'failed', 'message' => 'Unable to delete host']);
    }
}
