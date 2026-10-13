$(document).ready(function() {
    let table = $('#transactionsTable').DataTable({
        processing: true,
        serverSide: true,
        ajax: {
            url: 'http://localhost:5000/api/transactions',
            dataSrc: 'data',
            data: function(d) {
                return {
                    draw: d.draw,
                    page: Math.floor(d.start / d.length) + 1,
                    limit: d.length,
                    sort: d.columns[d.order[0].column].data,
                    order: d.order[0].dir,
                    search: d.search.value
                };
            }
        },
        columns: [
            { data: 'date' },
            { data: 'description' },
            { data: 'category' },
            {
                data: 'amount',
                render: function(data, type, row) {
                    return '$' + parseFloat(data).toFixed(2);
                }
            },
            {
                data: 'type',
                render: function(data) {
                    if (data === 'income') {
                        return '<span class="badge bg-success">Income</span>';
                    } else {
                        return '<span class="badge bg-danger">Expense</span>';
                    }
                }
            }
        ],
        order: [[0, 'desc']],
        pageLength: 25,
        lengthMenu: [[10, 25, 50, 100], [10, 25, 50, 100]],
        language: {
            processing: '<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div>'
        }
    });

    // Update summary totals
    function updateSummary() {
        $.ajax({
            url: 'http://localhost:5000/api/monthly-summary?months=12',
            type: 'GET',
            success: function(data) {
                let totalIncome = 0;
                let totalExpenses = 0;

                data.forEach(function(item) {
                    totalIncome += parseFloat(item.income);
                    totalExpenses += parseFloat(item.expenses);
                });

                $('#totalIncome').text('$' + totalIncome.toFixed(2));
                $('#totalExpenses').text('$' + totalExpenses.toFixed(2));
            },
            error: function(xhr, status, error) {
                console.error('Error fetching summary:', error);
            }
        });
    }

    updateSummary();
});
