<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Filterlog extends Model
{
    /** @use HasFactory<\Database\Factories\FilterlogFactory> */
    use HasFactory;

    protected $table = 'filterlog';

    public $timestamps = false;
}
