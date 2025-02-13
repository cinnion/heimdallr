@extends('layouts.app')

@section('title')
    Host Summary
@stop

@section('content')
    <h1>Ansible Host Summary</h1>

    <table id="ansible-host-summary" class="table table-striped table-hover">
        <thead></thead>
        <tfoot><tr><th></th><th></th><th></th><th></th><th></th><th></th><th></th><th>TOTAL USAGE:</th><th></th><th></th><th></th><th></th></tr></tfoot>
    </table>

    <script type="text/javascript">
        $(document).ready(function () {
            const table = $('#ansible-host-summary').DataTable({
                serverSide: true,
                processing: true,
                scrollX: true,
                ajax: {
                    url: '{{ route("ansible-host-summary.index") }}'
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
                'drawCallback': function(settings) {
                    let api = this.api();
                    var response = settings.json;

                    api.column(8).footer().innerHTML = response.cyteen_vm_cpu_usage;
                    api.column(9).footer().innerHTML = response.cyteen_vm_ram_usage;
                    api.column(10).footer().innerHTML = response.r720_vm_cpu_usage;
                    api.column(11).footer().innerHTML = response.r720_vm_ram_usage;
                }
            });



            $('#ansible-host-summary').on('click', '.delete-host', function() {
                const hostId = $(this).val();

                if (hostId) {
                    if (confirm('Are you sure you want to delete?')) {
                        $.ajax({
                            url: `{{ url('ansible-host-summary') }}/${hostId}`,
                            method: 'DELETE',
                            data: {
                                _token: '{{ csrf_token() }}',
                            },
                            success: function(response) {
                                if (response.status === 'success') {
                                    table.ajax.reload(null, false);
                                } else {
                                    alert(response.message);
                                }
                            },
                            error: function(error) {
                                alert('Something went wrong!');
                            }
                        });
                    }
                }
            });
        });
    </script>
@stop
