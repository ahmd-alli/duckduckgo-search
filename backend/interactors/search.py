from backend.service.duckduck_go import DuckDuckGo

def call(query: str):
    search = DuckDuckGo.search(query)
    search_result = DuckDuckGo.search_results(query)
    
    return {"search":search, "search_result":search_result}
    
