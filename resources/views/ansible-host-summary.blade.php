@extends('layout')

@section('title')
    Host Summary
@stop

@section('contents')
    <h1>Ansible Host Summary</h1>

    <table id="ansible-host-summary" border="1">

    </table>

    <script type="text/javascript">
        $(document).ready(function () {
            $('#ansible-host-summary').DataTable({
                serverSide: true,
                processing: true,
                ajax: {
                    url: '{{ route("ansible-host-summary") }}'
                },
                'columns': [
                    {
                        data: 'id',
                        name: 'id',
                        visible: false,
                        searchable: false,
                    },
                    {
                        data: 'hostname',
                        name: 'hostname',
                        title: 'Hostname',
                        width: '75px',
                    },
                    {
                        data: 'os_version',
                        name: 'os_version',
                        title: 'OS version',
                        width: '120px',
                    },
                    {
                        data: 'python3_version',
                        name: 'python3_version',
                        title: 'Python3 version',
                        width: '120px',
                    },
                    {
                        data: 'status_notes',
                        name: 'status_notes',
                        title: 'Status Notes',
                        width: '120px',
                    },
                    {
                        data: 'virtual_disk_size_mb',
                        name: 'virtual_disk_size_mb',
                        title: 'Virtual Disk Size (MB)',
                        width: '120px',
                    },
                    {
                        data: 'special_notes',
                        name: 'special_notes',
                        title: 'Special notes',
                    },
                    {
                        data: 'running',
                        name: 'running',
                        title: 'Running',
                        width: '95px',
                    },
                    {
                        data: 'cyteen_vm_cpu_allocation',
                        name: 'cyteen_vm_cpu_allocation',
                        title: 'Cyteen VM CPU allocation',
                        width: '100px',
                    },
                    {
                        data: 'cyteen_vm_ram_allocation',
                        name: 'cyteen_vm_ram_allocation',
                        title: 'Cyteen VM RAM allocation',
                        width: '100px',
                    },
                    {
                        data: 'r720_vm_cpu_allocation',
                        name: 'r720_vm_cpu_allocation',
                        title: 'r720 VM CPU allocation',
                        width: '100px',
                    },
                    {
                        data: 'r720_vm_ram_allocation',
                        name: 'r720_vm_ram_allocation',
                        title: 'r720 VM RAM allocation',
                        width: '100px',
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
                    [1, 'asc'],
                ],
            })
        })
    </script>
@stop
