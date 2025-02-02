@extends('firewall.index')

@section('title')
    Firewall: Blackholes
@stop

@section('contents')
    <h1>Firewall Blackhole Summary</h1>

    <table id="blackhole-summary" border="1">

    </table>

    <script type="text/javascript">
        $(document).ready(function () {
            $('#blackhole-summary').DataTable({
                serverSide: true,
                processing: true,
                ajax: {
                    url: '{{ route("firewall.blackholes") }}'
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
                        defaultContent: '<a href="#" onclick="var id=this.closest(\'tr\').id; window.location.href=\'/applications/\' + id + \'/edit\';"><button>Edit</button></a>',
                        name: 'actions',
                        title: 'Actions',
                        width: '100px',
                        placeholder: true,
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
