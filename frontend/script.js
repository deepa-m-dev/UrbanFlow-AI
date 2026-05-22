

let trafficChart; // store chart instance globally

async function predictTraffic() {

  try {

    // ----------------------------
    // COLLECT INPUT DATA
    // ----------------------------
    const data = {
      hour: Number(document.getElementById("hour").value),
      day_of_week: Number(document.getElementById("day").value),
      vehicle_count: Number(document.getElementById("vehicle").value),
      weather: Number(document.getElementById("weather").value),
      accident: Number(document.getElementById("accident").value),
      road_type: Number(document.getElementById("road").value),
      event: Number(document.getElementById("event").value)
    };

    // ----------------------------
    // CALL BACKEND API
    // ----------------------------
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    });

    const result = await response.json();

    // ----------------------------
    // AI INSIGHT LOGIC
    // ----------------------------
    let insightText = "";

    if (result.predicted_congestion > 70) {
      insightText = "High congestion expected. Avoid peak hours (6–9 PM).";
    } else if (result.predicted_congestion > 40) {
      insightText = "Moderate traffic. Slight delays possible.";
    } else {
      insightText = "Low traffic. Smooth travel expected.";
    }

    // ----------------------------
    // UPDATE UI
    // ----------------------------
    document.getElementById("result").innerHTML = `
      🚦 Congestion: ${result.predicted_congestion.toFixed(2)}% <br>
      📍 Cluster: ${result.traffic_cluster}
      <div class="insight">
        🧠 AI Insight:<br>
        ${insightText}
      </div>
    `;

    // ----------------------------
    // UPDATE CHART
    // ----------------------------
    drawChart(result.predicted_congestion);

  } catch (error) {
    console.error("Error:", error);
    document.getElementById("result").innerHTML =
      "❌ Error connecting to server. Make sure backend is running.";
  }
}

// ----------------------------
// CHART FUNCTION (NO DUPLICATES)
// ----------------------------
function drawChart(value) {

  const ctx = document.getElementById('chart');

  // destroy old chart if exists
  if (trafficChart) {
    trafficChart.destroy();
  }

  trafficChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Morning', 'Afternoon', 'Evening', 'Night'],
      datasets: [{
        label: 'Traffic Trend Simulation',
        data: [
          value * 0.6,
          value * 0.8,
          value,
          value * 0.5
        ],
        borderColor: '#38bdf8',
        tension: 0.4,
        fill: true
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          labels: { color: 'white' }
        }
      },
      scales: {
        x: { ticks: { color: 'white' } },
        y: { ticks: { color: 'white' } }
      }
    }
  });
}
