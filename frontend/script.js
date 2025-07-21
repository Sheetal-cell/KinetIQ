async function fetchData() {
  const response = await fetch('http://localhost:5000/data');
  const data = await response.json();

  document.getElementById('battery').textContent = data.battery + '%';
  document.getElementById('energy').textContent = data.energy + ' Wh';
  document.getElementById('timestamp').textContent = data.timestamp;

  renderChart(data.voltageData);
}

function renderChart(voltageData) {
  const ctx = document.getElementById('voltageChart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: voltageData.map(d => d.time),
      datasets: [{
        label: 'Voltage (V)',
        data: voltageData.map(d => d.voltage),
        borderColor: '#00ffae',
        borderWidth: 2,
        pointRadius: 3,
        tension: 0.4
      }]
    },
    options: {
      scales: {
        x: { ticks: { color: 'white' } },
        y: { ticks: { color: 'white' } }
      },
      plugins: {
        legend: { labels: { color: 'white' } }
      }
    }
  });
}

fetchData();
