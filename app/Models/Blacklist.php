<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Blacklist extends Model
{
    /** @use HasFactory<\Database\Factories\BlacklistFactory> */
    use HasFactory;

    protected $fillable = [
        'blackhole',
    ];

    protected $table = 'blacklist';

    public $timestamps = false;
}
