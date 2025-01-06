import uvicorn
from fastapi import FastAPI
from backend.routes import search

# App.
app = FastAPI()
app.include_router(search.router)

# Run.
uvicorn.run(app, host="0.0.0.0", port=8000)
