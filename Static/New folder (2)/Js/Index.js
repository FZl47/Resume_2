let AllChartSkills = document.querySelectorAll('[ChartSkill]')
for (let Skill of AllChartSkills) {
    SetChart(Skill)
}

function SetChart(Canvas) {
    if (Canvas) {
        let Label = Canvas.getAttribute('TitleSkill') || 'Unknown'
        let ValuePercent = parseInt(Canvas.getAttribute('ValuePercent'))
        let ChartCircle = new Chart(Canvas, {
            type: 'doughnut',
            data: {
                labels: [Label, 'null'],
                datasets: [{
                    label: "%",
                    backgroundColor: ["#41beba"],
                    data: [ValuePercent, 100 - ValuePercent]
                }]
            },
            plugins: [{
                /*beforeDraw: function (chart) {
                    var width = chart.chart.width,
                        height = chart.chart.height,
                        ctx = chart.chart.ctx;

                    ctx.restore();
                    var fontSize = (height / 150).toFixed(2);
                    ctx.font = fontSize + "em sans-serif";
                    ctx.fillStyle = "#9b9b9b";
                    ctx.textBaseline = "middle";
                    var text = "",
                        textX = Math.round((width - ctx.measureText(text).width) / 2),
                        textY = height / 2;

                    ctx.fillText(text, textX, textY);
                    ctx.save();
                }*/
            }],
            options: {
                legend: {
                    display: false,
                },
                responsive: true,
                maintainAspectRatio: false,
                cutoutPercentage: 60
            }
        });
    }
}
