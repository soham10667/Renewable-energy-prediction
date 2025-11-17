// ====== API base URL (Flask backend) ======
const API_BASE = "http://127.0.0.1:5000/api";

// ====== DOM elements ======
const form = document.getElementById("predict-form");
const predictionValue = document.getElementById("prediction-value");

// ====== Chart.js data arrays ======
const predictionLabels = [];   // X-axis: Run 1, Run 2, ...
const predictionData = [];     // Y-axis: prediction in kW

// ====== Create Chart.js line chart (initially empty) ======
let predictionChart;

const canvas = document.getElementById("predictionChart");
if (canvas) {
  const ctx = canvas.getContext("2d");
  predictionChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: predictionLabels,
      datasets: [
        {
          label: "Predicted Power Output (kW)",
          data: predictionData,
          borderColor: "#22c55e",
          backgroundColor: "rgba(34,197,94,0.15)",
          tension: 0.3,
          pointRadius: 3,
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          labels: {
            color: "#ffffff",
          },
        },
      },
      scales: {
        x: {
          ticks: { color: "#a3a3a3" },
          grid: { color: "rgba(255,255,255,0.05)" },
        },
        y: {
          beginAtZero: true,
          ticks: { color: "#a3a3a3" },
          grid: { color: "rgba(255,255,255,0.05)" },
        },
      },
    },
  });
}

// ====== Form submit handler (prediction + graph update) ======
if (form) {
  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    // Payload keys MUST match app.py: temperature, wind_speed, humidity, solar_irradiance
    const payload = {
      temperature: parseFloat(document.getElementById("temperature").value),
      wind_speed: parseFloat(document.getElementById("wind_speed").value),
      humidity: parseFloat(document.getElementById("humidity").value),
      solar_irradiance: parseFloat(
        document.getElementById("solar_irradiance").value
      ),
    };

    predictionValue.textContent = "Predicting...";

    try {
      const res = await fetch(`${API_BASE}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = await res.json();

      if (!res.ok) {
        predictionValue.textContent = `Error: ${data.error || "Request failed"}`;
        return;
      }

      const value = Number(data.prediction).toFixed(2);
      predictionValue.textContent = `Predicted power output: ${value} kW`;

      // ====== Update graph here ======
      if (predictionChart) {
        // Label like: Run 1, Run 2, ...
        predictionLabels.push(`Run ${predictionLabels.length + 1}`);
        // Y-axis value
        predictionData.push(parseFloat(value));
        predictionChart.update();
      }
    } catch (err) {
      console.error(err);
      predictionValue.textContent = "Error connecting to backend.";
    }
  });
}
