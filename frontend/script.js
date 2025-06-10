// Placeholder script for XRAP frontend

document.getElementById('send').addEventListener('click', () => {
    const cmd = document.getElementById('command').value;
    console.log('Enviar comando:', cmd);
    // TODO: send command to backend
});

function refreshTelemetry() {
    console.log('Refrescando telemetría...');
    // TODO: fetch telemetry from backend
}

setInterval(refreshTelemetry, 3000);
