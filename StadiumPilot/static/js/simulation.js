document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.querySelector('.chat-container');
    if (!chatContainer) return;
    
    const role = chatContainer.dataset.role;
    let seenEvents = new Set();

    function pollSimulationEvents() {
        fetch('/api/simulation/events')
        .then(res => res.json())
        .then(data => {
            const events = data.events;
            // If events array is empty, clear our local seen cache to reset
            if (events.length === 0) {
                seenEvents.clear();
                // Optionally clear active alerts in UI
                const alertsList = document.getElementById('security-alerts');
                if (alertsList) {
                    alertsList.innerHTML = '<li class="alert-item"><i class="fa-solid fa-check text-green"></i> All systems normal</li>';
                }
                return;
            }

            events.forEach(event => {
                if (!seenEvents.has(event.id)) {
                    seenEvents.add(event.id);
                    
                    // Show role-specific notification toast
                    const roleMessageKey = `${role}_message`;
                    const roleMessage = event[roleMessageKey];
                    
                    if (roleMessage) {
                        showToast(`<strong>${event.title}</strong><br>${roleMessage}`, 'error');
                        
                        // If it's the security dashboard, add to active alerts
                        if (role === 'security') {
                            const alertsList = document.getElementById('security-alerts');
                            if (alertsList) {
                                // Remove "All normal" if present
                                if (alertsList.innerHTML.includes('All systems normal')) {
                                    alertsList.innerHTML = '';
                                }
                                alertsList.innerHTML += `
                                    <li class="alert-item" style="color: var(--danger);">
                                        <i class="fa-solid fa-triangle-exclamation"></i> ${event.title}: ${roleMessage}
                                    </li>
                                `;
                            }
                        }
                    }
                }
            });
        })
        .catch(err => console.error("Error polling simulation events:", err));
    }

    // Poll every 5 seconds for simulation events
    setInterval(pollSimulationEvents, 5000);
});
