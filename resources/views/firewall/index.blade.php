@extends('layout')

@section('title')
    Firewall
@stop

@section('sub-nav')
    <nav>
        <a href="{{ @route('firewall.blackholes') }}">Blackholes</a> |
        <a href="{{ @route('firewall.heavy-hitters') }}">Heavy Hitters</a>
    </nav>
@stop

@section('contents')
    <h1>Firewall Summary</h1>
@stop
