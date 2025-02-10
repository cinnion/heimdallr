@extends('firewall.index')

@section('title')
    Firewall: Heavy Hitters
@stop

@section('content')
    <h1>Firewall Heavy Hitter Summary</h1>

    <table id="heavy-hitters" class="table table-striped table-hover">
    </table>

    <script type="text/javascript">
        $(document).ready(function () {
            const datatable = $('#heavy-hitters').DataTable({
                serverSide: true,
                processing: true,
                ajax: {
                    url: '{{ route("heavyhitters.index") }}',
                    data: function(payload) {
                        const includeBlackholed = $('#withBlackholed').is(':checked');
                        payload.includeBlackholed = includeBlackholed;
                    },
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
                    top2end: function() {
                        let withBlackholed = document.createElement("div");
                        withBlackholed.innerHTML = '<input type="checkbox" id="withBlackholed" name="withBlackholed" value="Yes">&nbsp;With Blackholed Hitters ';

                        return withBlackholed;
                    },
                    topStart: 'pageLength',
                    topEnd: 'search',
                    bottomStart: 'info',
                    bottomEnd: 'paging',
                },
                'initComplete': function() {
                    const inputSearchRow = $('#heavy-hitters thead tr').clone(true).appendTo('#heavy-hitters thead');

                    inputSearchRow.find('th').each(function(index) {
                        if (index === 0 || index === inputSearchRow.find('th').length -1) {
                            $(this).html('');
                        } else {
                            $(this).html('<input type="text" class="form-control search-input" placeholder="Search..." />');
                        }

                    });

                    $('#heavy-hitters thead tr:nth-child(2) th').click(function(event) {
                        event.stopPropagation();
                    });

                    $('.search-input').on('keyup change', function() {
                        const columnIndex = $(this).parent().index();
                        const searchedTerms = $(this).val().trim();

                        datatable.column(columnIndex).search(searchedTerms).draw();
                    });

                    $('#withBlackholed').on('change', function() {
                        datatable.draw();
                    })
                }
            });

            $('table#heavy-hitters').on('click', '.add-blackhole', function() {
                const cidrBlock = $(this).val();
                console.log(cidrBlock);

                if (cidrBlock) {
                    if (confirm('Are you sure you want to block ' + cidrBlock + ' ?')) {
                        $.ajax({
                            url: `{{ route('blackholes.store') }}`,
                            method: 'POST',
                            data: {
                                _token: '{{ csrf_token() }}',
                                blackhole: cidrBlock,
                            },
                            success: function(response) {
                                if (response.status === 'success') {
                                    datatable.ajax.reload(null, false);
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
            })
        });
    </script>
@stop
