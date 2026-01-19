import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("API_KEY")

@app.get("/")
def open_resource():
    return { "msg": "Hello from Derya!!", "v": "0.1" }

@app.get("/protected")
def secret_resource(api_key: str):
    if not api_key or api_key != API_KEY:
        return JSONResponse(status_code=401, content={"msg": "Unauthorized"})
    return {"msg": "This is a protected resource!!", "api_key": api_key}