import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from backend.routes import search

# Load the .env file.
load_dotenv()

# App.
app = FastAPI()
app.include_router(search.router)

# Run.
uvicorn.run(app, host="0.0.0.0", port=8000)
