// JavaScript code
document.addEventListener('DOMContentLoaded', function() {
    const chatbotIcon = document.getElementById('chatbot-icon');
    const chatWindow = document.getElementById('chat-window');
    const closeChatButton = document.getElementById('close-chat');
    const chatInput = document.getElementById('chat-input');
    const chatMessages = document.getElementById('chat-messages');
    const sendMessageButton = document.getElementById('send-message');

    // Event listener for chatbot icon click
    chatbotIcon.addEventListener('click', () => {
        chatWindow.style.display = 'block';
    });

    // Event listener for close chat button click
    closeChatButton.addEventListener('click', () => {
        chatWindow.style.display = 'none';
    });

    // Function to send message
    function sendMessage() {
        const messageText = chatInput.value.trim();

        if (messageText !== '') {
            // Create a new message element
            const newMessage = document.createElement('div');
            newMessage.textContent = messageText;

            // Append the new message to the chat messages container
            chatMessages.appendChild(newMessage);

            // Clear the input field after sending the message
            chatInput.value = '';
        }
    }

    // Event listener for send message button click
    sendMessageButton.addEventListener('click', sendMessage);

    // Function to handle sending message on Enter key press
    chatInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });
});
