<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;

class Filterlog extends ReadOnlyModel
{
    /** @use HasFactory<\Database\Factories\FilterlogFactory> */
    use HasFactory;

    protected $table = 'filterlog';

    public $timestamps = false;
}
