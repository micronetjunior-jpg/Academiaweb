const express = require("express");
const path = require("path");

const app = express();
const PUERTO = 80;

// Servir archivos estáticos desde la carpeta "public"
app.use(express.static("web"));


app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "web", "index.htm"));
});

app.listen(PUERTO, () => {
  console.log(`Servidor corriendo en http://localhost:${PUERTO}`);
});