from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

@asynccontextmanager
async def lifespan(app: FastAPI):
    print()
    print("Starting Main Server at port 80")

    app.mount("/web", StaticFiles(directory="/app/html"), name="web")

    app.mount("/static", StaticFiles(directory="/app/html/static"), name="static")

    yield

    print("Main Server detenido")

app = FastAPI(lifespan=lifespan)


@app.get("/.well-known/acme-challenge/{token}")
async def acme_challenge(token: str):
    return {"status": "ok"}

# Ruta raíz → index.html
@app.get("/")
def root():
    #return FileResponse(FRONTEND_DIR / "index.htm")
    return FileResponse("/app/html/index.htm") 


