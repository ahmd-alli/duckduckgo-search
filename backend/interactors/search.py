from backend.service.duckduck_go import DuckDuckGo


def call(query: str, keyword):
    if keyword == None:
        keyword = ""

    search = DuckDuckGo.search(query)
    search_result = DuckDuckGo.search_results(query, keyword)

    return {"search": search, "search_result": search_result}
