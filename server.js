const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.use(require('helmet')());
app.use(require('cors')());
app.use(require('morgan')('combined'));

app.post('/submit', (req, res) => {
    const { name, email, message } = req.body;

    if (!name || !email || !message) {
        return res.status(400).send('All fields are required.');
    }

    try {
        console.log(`Received: ${name}, ${email}, ${message}`);
        res.send('Thank you for contacting us!');
    } catch (error) {
        console.error('Error handling form submission:', error);
        res.status(500).send('Something went wrong. Please try again later.');
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
