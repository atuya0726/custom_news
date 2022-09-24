const express = require('express');
const yahoo   = require('./scraping/yahoo.js')

// Constants
const PORT = 80;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/data', async (req, res) => {
  const data = await yahoo.yahooScraping()
  res.send(data);
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);