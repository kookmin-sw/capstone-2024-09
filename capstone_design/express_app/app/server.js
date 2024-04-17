const express = require('express');
const app = express();
const port = 3001;
const axios = require('axios');

// React 프런트엔드 빌드 결과물 서빙
app.use(express.static('build'));

app.get('/api/data', async (req, res) => {
    res.send({ express: 'Hello From Express' });
    // try {
    //     const response = await axios.get('http://localhost:5000/api/data');
    //     res.json(response.data);
    // } catch (error) {
    //     res.status(500).json({ error: 'Failed to fetch data' });
    // }
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});