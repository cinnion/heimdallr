@extends('layouts.app')

@section('title')
    Firewall
@stop

@section('sub-nav')
    <nav>
        <a href="{{ @route('blackholes.index') }}">Blackholes</a> |
        <a href="{{ @route('heavyhitters.index') }}">Heavy Hitters</a>
    </nav>
@stop

@section('content')
    <h1>Firewall Summary</h1>
@stop
