$(document).ready(function() {
    // Chart instances
    let pieChart, barChart, lineChart;

    // Colors
    const colors = {
        blue: '#0d6efd',
        green: '#198754',
        red: '#dc3545',
        yellow: '#ffc107',
        purple: '#6f42c1',
        orange: '#fd7e14',
        teal: '#20c997',
        pink: '#d63384'
    };

    // 1. Pie Chart: Expenses by Category
    function loadPieChart() {
        $.ajax({
            url: 'http://localhost:5000/api/category-summary',
            type: 'GET',
            success: function(data) {
                const categories = data.map(item => item.category);
                const totals = data.map(item => item.total);

                if (pieChart) {
                    pieChart.destroy();
                }

                const ctx = document.getElementById('pieChart').getContext('2d');
                pieChart = new Chart(ctx, {
                    type: 'pie',
                    data: {
                        labels: categories,
                        datasets: [{
                            data: totals,
                            backgroundColor: [
                                colors.blue, colors.green, colors.red,
                                colors.yellow, colors.purple, colors.orange,
                                colors.teal, colors.pink
                            ],
                            borderWidth: 2,
                            borderColor: '#fff'
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                position: 'bottom',
                                labels: {
                                    boxWidth: 12,
                                    padding: 10
                                }
                            }
                        }
                    }
                });
            },
            error: function(xhr, status, error) {
                console.error('Error loading pie chart:', error);
            }
        });
    }

    // 2. Bar Chart: Monthly Income vs Expenses
    function loadBarChart() {
        $.ajax({
            url: 'http://localhost:5000/api/monthly-summary?months=6',
            type: 'GET',
            success: function(data) {
                const months = data.map(item => item.month);
                const incomes = data.map(item => item.income);
                const expenses = data.map(item => item.expenses);

                if (barChart) {
                    barChart.destroy();
                }

                const ctx = document.getElementById('barChart').getContext('2d');
                barChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: months,
                        datasets: [
                            {
                                label: 'Income',
                                data: incomes,
                                backgroundColor: colors.green,
                                borderRadius: 4
                            },
                            {
                                label: 'Expenses',
                                data: expenses,
                                backgroundColor: colors.red,
                                borderRadius: 4
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                position: 'top'
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                ticks: {
                                    callback: function(value) {
                                        return '$' + value.toFixed(0);
                                    }
                                }
                            }
                        }
                    }
                });
            },
            error: function(xhr, status, error) {
                console.error('Error loading bar chart:', error);
            }
        });
    }

    // 3. Line Chart: Spending Trends
    function loadLineChart() {
        $.ajax({
            url: 'http://localhost:5000/api/trends?period=30&type=expense',
            type: 'GET',
            success: function(data) {
                const dates = data.map(item => item.date);
                const totals = data.map(item => item.total);

                if (lineChart) {
                    lineChart.destroy();
                }

                const ctx = document.getElementById('lineChart').getContext('2d');
                lineChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: dates,
                        datasets: [{
                            label: 'Daily Spending',
                            data: totals,
                            borderColor: colors.blue,
                            backgroundColor: colors.blue + '20',
                            fill: true,
                            tension: 0.3,
                            pointRadius: 2,
                            pointBackgroundColor: colors.blue
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                display: true,
                                position: 'top'
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                ticks: {
                                    callback: function(value) {
                                        return '$' + value.toFixed(0);
                                    }
                                }
                            }
                        }
                    }
                });
            },
            error: function(xhr, status, error) {
                console.error('Error loading line chart:', error);
            }
        });
    }

    // 4. Load Summary Cards
    function loadSummaryCards() {
        $.ajax({
            url: 'http://localhost:5000/api/monthly-summary?months=12',
            type: 'GET',
            success: function(data) {
                let totalIncome = 0;
                let totalExpenses = 0;
                let count = 0;

                data.forEach(function(item) {
                    totalIncome += parseFloat(item.income);
                    totalExpenses += parseFloat(item.expenses);
                    count += 1;
                });

                const netSavings = totalIncome - totalExpenses;

                $('#totalIncomeDisplay').text('$' + totalIncome.toFixed(2));
                $('#totalExpensesDisplay').text('$' + totalExpenses.toFixed(2));
                $('#netSavingsDisplay').text('$' + netSavings.toFixed(2));
                $('#transactionCount').text(count * 8); // rough estimate
            },
            error: function(xhr, status, error) {
                console.error('Error loading summary cards:', error);
            }
        });
    }

    // Load all charts
    loadPieChart();
    loadBarChart();
    loadLineChart();
    loadSummaryCards();

    // Refresh charts every 60 seconds (optional)
    // setInterval(() => {
    //     loadPieChart();
    //     loadBarChart();
    //     loadLineChart();
    //     loadSummaryCards();
    // }, 60000);
});