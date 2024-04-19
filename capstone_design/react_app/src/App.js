import './App.css';
import React, { useState, useEffect } from 'react';
import ChatBot from "./components/Chatbot.js";

function App() {
    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('/api/data');
                const data = await response.json();
                setData(data);
                console.log(data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div>
            <ChatBot/>
        </div>
    );
}

export default App;
