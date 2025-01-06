from backend.service.duckduck_go import DuckDuckGo

def call(query: str) -> str:
    return DuckDuckGo.search(query)
