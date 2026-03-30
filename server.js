const express = require("express");

const app = express();
const PUERTO = 80;

// Servir archivos estáticos desde la carpeta "public"
app.use(express.static("public"));

app.listen(PUERTO, () => {
  console.log(`Servidor corriendo en http://localhost:${PUERTO}`);
});