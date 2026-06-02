let bitcoinChart = null;

function renderChart(data) {

    const canvas =
        document.getElementById(
            "bitcoin-chart"
        );

    const ctx =
        canvas.getContext("2d");

    if (bitcoinChart) {
        bitcoinChart.destroy();
    }

    bitcoinChart = new Chart(ctx, {

        type: "line",

        data: {

            labels: data.x,

            datasets: [

                {
                    label: "Precio Bitcoin",

                    data: data.y,

                    borderColor:
                        "#2563eb",

                    backgroundColor:
                        "rgba(37,99,235,.15)",

                    borderWidth: 3,

                    pointRadius: 4,

                    pointHoverRadius: 7,

                    pointBorderWidth: 2,

                    tension: 0.35,

                    fill: false
                },

                {
                    label: "Regresión Lineal",

                    data: data.predictions,

                    borderColor:
                        "#ef4444",

                    backgroundColor:
                        "rgba(239,68,68,.1)",

                    borderWidth: 3,

                    pointRadius: 0,

                    pointHoverRadius: 0,

                    tension: 0,

                    fill: false
                }
            ]
        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            interaction: {

                intersect: false,

                mode: "index"
            },

            animation: {

                duration: 1800,

                easing: "easeOutQuart"
            },

            plugins: {

                legend: {

                    position: "top",

                    labels: {

                        color: "#1e293b",

                        font: {

                            size: 14,

                            weight: "600"
                        },

                        padding: 20
                    }
                },

                title: {

                    display: true,

                    text:
                        "Precio Bitcoin vs Recta de Regresión",

                    color: "#0f172a",

                    font: {

                        size: 20,

                        weight: "bold"
                    },

                    padding: {

                        bottom: 20
                    }
                },

                tooltip: {

                    backgroundColor:
                        "#0f172a",

                    titleColor:
                        "#ffffff",

                    bodyColor:
                        "#ffffff",

                    padding: 12,

                    cornerRadius: 10,

                    displayColors: true,

                    callbacks: {

                        label: function(context) {

                            return (
                                context.dataset.label +
                                ": $" +
                                Number(
                                    context.parsed.y
                                ).toLocaleString(
                                    "es-CO",
                                    {
                                        minimumFractionDigits: 2,
                                        maximumFractionDigits: 2
                                    }
                                )
                            );
                        }
                    }
                }
            },

            scales: {

                x: {

                    title: {

                        display: true,

                        text: "Día",

                        color: "#334155",

                        font: {

                            size: 14,

                            weight: "600"
                        }
                    },

                    ticks: {

                        color: "#64748b"
                    },

                    grid: {

                        color:
                            "rgba(148,163,184,.15)"
                    }
                },

                y: {

                    title: {

                        display: true,

                        text: "Precio USD",

                        color: "#334155",

                        font: {

                            size: 14,

                            weight: "600"
                        }
                    },

                    ticks: {

                        color: "#64748b",

                        callback: function(value) {

                            return "$" +
                                Number(value)
                                    .toLocaleString(
                                        "es-CO"
                                    );
                        }
                    },

                    grid: {

                        color:
                            "rgba(148,163,184,.15)"
                    }
                }
            }
        }
    });
}