document.addEventListener('DOMContentLoaded', () => {
    if (typeof chartData !== 'undefined') {
        // Theme variables for charts
        const isDarkMode = !document.body.classList.contains('light-mode');
        const textColor = isDarkMode ? '#f8fafc' : '#0f172a';
        const gridColor = isDarkMode ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.1)';

        Chart.defaults.color = textColor;
        Chart.defaults.borderColor = gridColor;

        // Density Chart
        const ctxDensity = document.getElementById('densityChart').getContext('2d');
        new Chart(ctxDensity, {
            type: 'bar',
            data: {
                labels: chartData.crowd_density.labels,
                datasets: [{
                    label: 'Crowd Density (%)',
                    data: chartData.crowd_density.data,
                    backgroundColor: 'rgba(59, 130, 246, 0.7)',
                    borderColor: 'rgba(59, 130, 246, 1)',
                    borderWidth: 1
                }]
            },
            options: { responsive: true, maintainAspectRatio: false }
        });

        // Incident Trend Chart
        const ctxIncident = document.getElementById('incidentChart').getContext('2d');
        new Chart(ctxIncident, {
            type: 'line',
            data: {
                labels: chartData.incident_trends.labels,
                datasets: [{
                    label: 'Incidents Reported',
                    data: chartData.incident_trends.data,
                    backgroundColor: 'rgba(239, 68, 68, 0.2)',
                    borderColor: 'rgba(239, 68, 68, 1)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.3
                }]
            },
            options: { responsive: true, maintainAspectRatio: false }
        });
    }
});
