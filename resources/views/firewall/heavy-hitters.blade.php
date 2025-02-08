@extends('firewall.index')

@section('title')
    Firewall: Heavy Hitters
@stop

@section('contents')
    <h1>Firewall Heavy Hitter Summary</h1>

    <table id="heavy-hitters" class="table table-striped table-hover">
    </table>

    <script type="text/javascript">
        $(document).ready(function () {
            $('#heavy-hitters').DataTable({
                serverSide: true,
                processing: true,
                ajax: {
                    url: '{{ route("heavyhitters.index") }}'
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
                        width: '100px',
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
                        width: '100px',
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
                        data: 'action',
                        name: 'action',
                        title: 'Actions',
                        width: '200px',
                        orderable: false,
                        searchable: false,
                    }
                ],
                'order': [
                    [0, 'desc'],
                ],
                'layout': {
                    topStart: 'pageLength',
                    topEnd: 'search',
                    bottomStart: 'info',
                    bottomEnd: 'paging',
                },
                'initComplete': function() {
                    $('#heavy-hitters thead tr').clone(true).appendTo('#heavy-hitters thead');

                    this.api()
                        .columns()
                        .every(function() {
                            let column = this;
                            let title = column.header(1).textContent;

                            if (column.orderable()) {
                                // Create input element
                                let input = document.createElement('input');
                                input.placeholder = title;
                                column.header(1).replaceChildren(input);

                                // Event listener for user input.
                                input.addEventListener('keyup', () => {
                                    if (column.search() !== this.value) {
                                        column.search(input.value).draw();
                                    }
                                });
                            } else {
                                column.header(1).text('');
                            }
                        });
                }
            });

            $('table#heavy-hitters').on('click', '.add-blackhole', function() {
                const cidrBlock = $(this).val();
                console.log(cidrBlock);
            })
        });
    </script>
@stop
