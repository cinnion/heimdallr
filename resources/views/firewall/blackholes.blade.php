@extends('firewall.index')

@section('title')
    Firewall: Blackholes
@stop

@section('content')
    <h1>Firewall Blackhole Summary</h1>

    <table id="blackhole-summary" class="table table-striped table-hover">

    </table>

    <script type="text/javascript">
        $(document).ready(function () {
            $('#blackhole-summary').DataTable({
                serverSide: true,
                processing: true,
                ajax: {
                    url: '{{ route("blackholes.index") }}'
                },
                'columns': [
                    {
                        data: 'id',
                        name: 'id',
                        visible: false,
                        searchable: false,
                    },
                    {
                        data: 'blackhole',
                        name: 'blackhole',
                        title: 'Blackhole CIDR block',
                        width: '400px',
                    },
                    {
                        data: 'action',
                        name: 'action',
                        title: 'Actions',
                        width: '100px',
                        orderable: false,
                        searchable: false,
                    }
                ],
                'order': [
                    [1, 'asc'],
                ],
            })
        })
    </script>
@stop
