document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.querySelector('.chat-container');
    if (!chatContainer) return;

    const role = chatContainer.dataset.role;
    const input = document.getElementById('chat-input');
    const sendBtn = document.getElementById('send-btn');
    const messagesContainer = document.getElementById('chat-messages');

    function addMessage(content, sender) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${sender}-message`;
        msgDiv.innerHTML = `<div class="msg-content">${content}</div>`;
        messagesContainer.appendChild(msgDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function sendMessage(text) {
        if (!text.trim()) return;
        addMessage(text, 'user');
        input.value = '';

        // Add loading state
        const loadingId = 'loading-' + Date.now();
        const loadingMsg = document.createElement('div');
        loadingMsg.className = 'message ai-message';
        loadingMsg.id = loadingId;
        loadingMsg.innerHTML = `<div class="msg-content"><i class="fa-solid fa-circle-notch fa-spin"></i> Thinking...</div>`;
        messagesContainer.appendChild(loadingMsg);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;

        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: text, role: role })
        })
        .then(res => res.json())
        .then(data => {
            document.getElementById(loadingId).remove();
            addMessage(data.response, 'ai');
        })
        .catch(err => {
            document.getElementById(loadingId).remove();
            addMessage("Sorry, I encountered an error. Please try again.", 'ai');
            console.error(err);
        });
    }

    sendBtn.addEventListener('click', () => sendMessage(input.value));
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage(input.value);
    });

    // Expose quick message function to global scope for buttons
    window.sendQuickMessage = function(text) {
        sendMessage(text);
    };
});
