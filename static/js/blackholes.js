$(document).ready(function () {
    const table = $('#blackholes').DataTable({
        ajax: {
            url: '/api/firewall/blackholes',
            dataSrc: 'blackholes'
        },
        serverSide: true,
        processing: true,
        stateSave: true,
        rowId: 'id',
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
                name: 'edit',
                title: 'Actions',
                width: '100px',
                placeholder: true,
            }
        ],
        'order': [
            [1, 'asc'],
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
    });
});