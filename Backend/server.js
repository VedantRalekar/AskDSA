const express = require("express");
const cors = require("cors");
const axios = require("axios");
const PORT = 3000;

const app = express();

app.use(cors());
app.use(express.json());

// Forward request to FastAPI
app.post("/api/ask", async (req, res) => {

    try {

        const { question } = req.body;
        const response = await axios.post("http://localhost:8000/ask",{question});

        res.json(response.data);

    } catch (err) {

        console.error(err.message);
        res.status(500).json({
            error: "Unable to fetch response from RAG"
        });

    }

});


app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});