// server.js
const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

// Serve static files (e.g., CSS, JS, images)
app.use(express.static(path.join(__dirname, 'src')));

// Route to serve the index.html
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'src', 'index.html'));
});

// Start server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
