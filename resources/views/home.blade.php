@extends('layouts.app')

@section('title')
    Home
@stop

@section('content')
    <div class="alert alert-info">
        <strong>Note</strong>: Some parts of this application are doing complex queries involving tens of millions of
        records, so they may take a few seconds to complete loading.
    </div>
@stop
