const express = require('express');
const cors = require('cors');
const app = express();
const port = 3001;
const axios = require('axios');

// React 프런트엔드 빌드 결과물 서빙
app.use(express.static('build'));
app.use(cors({ credentials: true, origin: "http://react_app:3000" }));

app.get('/api/chat', async (req, res) => {
    const { messages } = req.body;

    try {
        const response = await axios.post('http://flask_app:5000/api/chat', { messages });
        res.json(response.data);
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ error: 'An error occurred while fetching the response' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});