from fastapi import APIRouter
from backend.interactors import search as search_interactor

# Create a router.
router = APIRouter(tags=["search"], prefix="/api")


@router.get("/search/")
async def search(query: str, keyword: str = None):
    return search_interactor.call(query, keyword)
