import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
    const [data] = useState([{}])
    // React 컴포넌트
    useEffect(() => {
        fetch('/api/data')
            .then(response => response.json())
            .then(data => console.log(data));
    }, []);
    return (
      <div>
        {(typeof data.members === 'undefined') ? (
            <p>Loading ... </p>
        ) : (
            data.members.map((member, i) => (
                <p key={i}>{member}</p>
            ))
        )}
      </div>
    );
}

export default App;
