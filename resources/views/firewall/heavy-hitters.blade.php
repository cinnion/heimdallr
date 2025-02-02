@extends('firewall.index')

@section('title')
    Firewall: Heavy Hitters
@stop

@section('contents')
    <h1>Firewall Heavy Hitter Summary</h1>

    <table id="heavy-hitters" border="1">

    </table>

    <script type="text/javascript">
        $(document).ready(function () {
            $('#heavy-hitters').DataTable({
                serverSide: true,
                processing: true,
                ajax: {
                    url: '{{ route("firewall.heavy-hitters") }}'
                },
                'columns': [
                    {
                        data: 'cnt',
                        name: 'cnt',
                        title: 'Count',
                        width: '100px',
                    },
                    {
                        data: 'tmstamp',
                        name: 'tmstamp',
                        title: 'Date',
                        width: '150px',
                    },
                    {
                        data: 'cidrBlock',
                        name: 'cidrBlock',
                        title: 'CIDR Block',
                        width: '150px',
                    },
                    {
                        data: 'rule_num',
                        name: 'rule_num',
                        title: 'Rule Number',
                        width: '150px',
                    },
                    {
                        data: 'blocked',
                        name: 'blocked',
                        title: 'Blocked',
                        width: '150px',
                    },
                    {
                        data: 'blocked_ports',
                        name: 'blocked_ports',
                        title: 'Blocked Ports',
                        width: '150px',
                    },
                    {
                        data: 'bh_id',
                        name: 'bh_id',
                        title: 'BH ID',
                        width: '100px',
                    },
                    {
                        data: 'blackhole',
                        name: 'blackhole',
                        title: 'Blackhole CIDR',
                    },
                    {
                        defaultContent: '<a href="#" onclick="var id=this.closest(\'tr\').id; window.location.href=\'/applications/\' + id + \'/edit\';"><button>Edit</button></a>',
                        name: 'edit',
                        title: 'Actions',
                        width: '100px',
                        placeholder: true,
                    }
                ],
                'order': [
                    [0, 'desc'],
                ],
                layout: {
                    top1End: function () {
                        let toolbar = document.createElement('div');
                        toolbar.innerHTML = '<a href="/firewall/new-blackhole/"><button id="add">Add</button></a>';

                        return toolbar;
                    },
                    topStart: 'pageLength',
                    topEnd: 'search',
                    bottomStart: 'info',
                    bottomEnd: 'paging',
                }
            })
        })
    </script>
@stop
