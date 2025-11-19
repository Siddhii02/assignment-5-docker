const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");
const cors = require("cors");
const path = require("path");

const app = express();

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Serve HTML files
app.use(express.static(path.join(__dirname, "public")));

// Form submit route (calls Flask backend)
app.post("/submit", async (req, res) => {
  try {
    const result = await axios.post("http://localhost:9000/submit", req.body);

    if (result.data.status === "success") {
      res.redirect("/success.html");
    } else {
      res.send("Error submitting data");
    }
  } catch (err) {
    console.log("Error:", err.message);
    res.send("Backend error");
  }
});

// Start server
app.listen(5000, () => {
  console.log("Frontend running on http://localhost:5000");
});
