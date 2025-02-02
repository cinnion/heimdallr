<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>{{ config('app.name', 'Heimdallr')}}: @yield('title')</title>

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.bunny.net">
    <!-- <link href="https://fonts.bunny.net/css?family=figtree:400,500,600&display=swap" rel="stylesheet" /> -->

    <!-- Styles / Scripts -->
    <link href="https://cdn.datatables.net/2.2.1/css/dataTables.bootstrap5.min.css" rel="stylesheet" />

    <script src="https://code.jquery.com/jquery-3.7.1.js"></script>
    <script src="https://cdn.datatables.net/2.2.1/js/dataTables.js"></script>
    <script src="https://cdn.datatables.net/2.2.1/js/dataTables.bootstrap5.min.js"></script>

    @vite(['resources/sass/app.scss', 'resources/js/app.js'])

</head>
<body>
    <nav>
        <a href="{{ @route('ansible-host-summary.index') }}">Ansible Host Summary</a> |
        <a href="{{ @route('firewall.index') }}">Firewall</a>
    </nav>
    @yield('sub-nav')

    <div class="container">
        @yield('contents')
    </div>
</body>
