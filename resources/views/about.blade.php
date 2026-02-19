@extends('layouts.app')

@section('title')
    About
@stop

@section('content')
    @if (isset($build_info['Error']))
        <div class="alert alert-warning">
        <strong>Error</strong>: {{ $build_info['Error'] }}
        </div>
    @endif

    <div>Build Number: {{ $build_info['BUILD_NUMBER'] }}</div>
    <div>Build ID: {{ $build_info['BUILD_ID'] }}</div>
    <div>Build URL: {{ $build_info['BUILD_URL'] }}</div>
    <div>Git Commit: {{ $build_info['GIT_COMMIT'] }}</div>
    <div>Git Branch: {{ $build_info['GIT_BRANCH'] }}</div>
    <div>Build Date: {{ $build_info['BUILD_DATE'] }}</div>
    <br/>

    <div>Number of firewall records: {{ number_format($filterlog_rows) }}</div>

@stop
