import React, { useState } from 'react';
import axios from 'axios';

function ChatBot() {
    const [messages, setMessages] = useState([]);
    const [inputMessage, setInputMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessages([...messages, { role: 'user', content: inputMessage }]);
        setInputMessage('');

        try {
            const response = await axios.post('/api/chat', { messages: [...messages, { role: 'user', content: inputMessage }] });
            setMessages([...messages, { role: 'user', content: inputMessage }, { role: 'assistant', content: response.data.result }]);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div>
            <h1>ChatBot</h1>
            <div>
                {messages.map((message, index) => (
                    <div key={index}>
                        <strong>{message.role}: </strong>
                        {message.content}
                    </div>
                ))}
            </div>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={inputMessage}
                    onChange={(e) => setInputMessage(e.target.value)}
                    placeholder="Type your message..."
                />
                <button type="submit">Send</button>
            </form>
        </div>
    );
}

export default ChatBot;