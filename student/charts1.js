

document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('bar').getContext('2d');
    
    var data = {
        labels: ['Available', 'Booked'],
        datasets: [{
            label: 'Available',
            data: [100, 40],
            backgroundColor: [
                'rgba(41, 155, 99, 1)',
                'rgba(54, 162, 235, 1)',
            ],
            borderColor: [
                'rgba(41, 155, 99, 1)',
                'rgba(54, 162, 235, 1)',
            ],
            borderWidth: 1,
        }],
    };

    var options = {
        responsive: true,
        scales: {
            x: {
                beginAtZero: true,
            },
            y: {
                beginAtZero: true,
            },
        },
    };

    var myChart = new Chart(ctx, {
        type: 'bar',
        data: data,
        options: options,
    });
});
