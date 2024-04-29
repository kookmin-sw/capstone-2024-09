import './App.css';
import React, {useState} from "react";

function App() {
    const [messages, setMessages] = useState([]);
    const [inputMessage, setInputMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newMessage = { role: 'user', content: inputMessage };
        const updatedMessages = [...messages, newMessage];

        try {
            const response = await fetch('http://localhost:5000/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
                body: JSON.stringify({ messages: updatedMessages }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            console.log(data);
        } catch (error) {
            console.error('Error:', error);
        }

        setMessages([...messages, newMessage]);
        setInputMessage('');
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
