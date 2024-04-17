const express = require('express');
const cors = require('cors');
const app = express();
const port = 3001;
const axios = require('axios');

// React 프런트엔드 빌드 결과물 서빙
app.use(express.static('build'));
app.use(cors({ credentials: true, origin: "develop.sung4854.com:3000" }));

app.get('/api/data', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/api/data');
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: 'Failed to fetch data' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});