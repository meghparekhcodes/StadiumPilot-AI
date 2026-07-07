document.addEventListener('DOMContentLoaded', () => {
    // Theme Toggle
    const themeBtn = document.getElementById('theme-toggle');
    themeBtn.addEventListener('click', () => {
        document.body.classList.toggle('light-mode');
        const icon = themeBtn.querySelector('i');
        if (document.body.classList.contains('light-mode')) {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        }
    });

    // Accessibility Panel Toggle
    const accessBtn = document.getElementById('accessibility-btn');
    const accessPanel = document.getElementById('accessibility-panel');
    accessBtn.addEventListener('click', () => {
        accessPanel.classList.toggle('hidden');
    });

    // High Contrast Toggle
    const hcToggle = document.getElementById('high-contrast-toggle');
    hcToggle.addEventListener('change', (e) => {
        if (e.target.checked) {
            document.body.classList.add('high-contrast');
        } else {
            document.body.classList.remove('high-contrast');
        }
    });

    // Large Text Toggle
    const ltToggle = document.getElementById('large-text-toggle');
    ltToggle.addEventListener('change', (e) => {
        if (e.target.checked) {
            document.body.classList.add('large-text');
        } else {
            document.body.classList.remove('large-text');
        }
    });
});

// Toast Notification System
function showToast(message, type = 'info') {
    const container = document.getElementById('toast-container');
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerHTML = `<i class="fa-solid fa-bell"></i> ${message}`;
    
    container.appendChild(toast);
    
    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
    }, 5000);
}
