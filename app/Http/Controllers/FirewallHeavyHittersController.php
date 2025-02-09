<?php

namespace App\Http\Controllers;

use App\Models\HeavyHitter;
use Illuminate\Http\Request;
use Illuminate\Support\Carbon;
use Yajra\DataTables\Facades\DataTables;

class FirewallHeavyHittersController extends Controller
{
    /**
     * Show a listing of the networks hitting the firewall.
     *
     * @param Request $request
     * @return \Illuminate\Contracts\View\Factory|\Illuminate\Contracts\View\View|\Illuminate\Foundation\Application|\Illuminate\Http\JsonResponse
     * @throws \Exception
     */
    public function index(Request $request)
    {
        if ($request->ajax()) {
            $heavy_hitters = HeavyHitter::query();

            $includeBlackholed = $request->includeBlackholed ?? 'false';
            if ($includeBlackholed == 'false') {
                $heavy_hitters->whereNull('bh_id');
            }

            return DataTables::eloquent($heavy_hitters)
                ->addColumn('tmstamp', function($hitter) {
                    return Carbon::parse($hitter->tmstamp)->format('Y-m-d');
                })
                ->addColumn('action', function ($hitter) {
                    $cidrStr = str_replace('/', '-', $hitter->cidrBlock);

                    $retval = '<a href="' . route('heavyhitters.detail', $cidrStr) . '" class="btn btn-success btn-sm" target="_blank">Details</a>';

                    if (empty($hitter->blackhole)) {
                        $retval .= '&nbsp;<button value="' . route('blackholes.add', $cidrStr) . '" class="btn btn-danger btn-sm add-blackhole" target="_blank">Add Blackhole</a>';
                    }
                    return $retval;
                })
                ->rawColumns(['action'])
                ->make(true);
        } else {
            return view('firewall.heavy-hitters');
        }
    }

    /**
     * Show the details for a given CIDR block
     */
    public function details(Request $request, string $cidrBlock)
    {
        $cidrBlock = str_replace('-', '/', $cidrBlock);
        dd($cidrBlock);
    }
}
