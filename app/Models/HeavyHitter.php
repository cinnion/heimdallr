<?php

namespace App\Models;

class HeavyHitter extends ReadOnlyModel
{
    protected $table = 'heavy_hitters';

    public $timestamps = false;
}
