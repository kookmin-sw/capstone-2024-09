import './App.css';
import React, {useState} from "react";

function App() {
    const [messages, setMessages] = useState([]);
    const [inputMessage, setInputMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newMessage = { role: 'user', content: inputMessage };
        setMessages([...messages, newMessage]);
        setInputMessage('');

        try {
            const response = await fetch('http://fastapi_app:5000/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ messages: [...messages, newMessage] }),
            });

            if (response.ok) {
                const data = await response.json();
                const assistantMessage = { role: 'assistant', content: data.result };
                setMessages([...messages, newMessage, assistantMessage]);
            } else {
                throw new Error('Network response was not ok');
            }
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

export default App;
