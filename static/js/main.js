var daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];
var closingPrice = ['300', '330', '307', '319', '291'];

var myChart = new Chart
    ("AMAZON",
        {
        type: line
        data:
            {
            labels: daysOfTheWeek
            datasets: [{
                data: closingPrice
                borderColor: "red",
                fill: false
                }]
            }
            options:
            {
                title:
                {
                    display: true,
                    text: "Weekly Stock Data for: *Stock Ticker*"
                }

            }
        }
    );




