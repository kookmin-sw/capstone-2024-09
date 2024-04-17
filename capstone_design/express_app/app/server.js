const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3001;

// React 프런트엔드 빌드 결과물 서빙
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }))

app.get('/api/hello', (req, res) => {
    res.send({ express: 'Hello From Express' });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});