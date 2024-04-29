import React, {useState} from "react";

export function ChatComponent() {
    const [messages, setMessages] = useState([]);
    const [inputMessage, setInputMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newMessage = { role: 'user', content: inputMessage };
        const updatedMessages = [...messages, newMessage];
        // 이거는 추 후에 분류형 AI에게 넘겨줄 데이터로 사용하며 될 듯 하다.

        try {
            const response = await fetch('http://develop.sung4854.com:5000/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
                body: JSON.stringify({ messages: newMessage }),
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