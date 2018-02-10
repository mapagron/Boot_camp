
        
Highcharts.chart('voluntering', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'National Voluntering Categories (2015)'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                style: {
                    color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                }
            }
        }
    },
    series: [{
        name: 'Percentage',
        colorByPoint: true,
        data: [{
            name: 'Civic, political, professional or international',
            y: 5
        }, {
            name: 'Educational or youth service',
            y: 26,
            sliced: true,
            selected: true
        }, {
            name: 'Hospital or other health',
            y: 7
        }, {
            name: 'Religious',
            y: 34
        }, {
            name: 'Social or community service',
            y:15
        }, {
            name: 'Sports',
            y: 4
        }, {
            name: 'Other',
            y: 9
        }]
        
    }]
});
