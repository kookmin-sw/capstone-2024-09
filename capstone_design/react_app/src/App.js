import './App.css';
import React, { useState, useEffect } from 'react';

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
            {data ? (
                <p>Data from Express: {data.data}</p>
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
}

export default App;
