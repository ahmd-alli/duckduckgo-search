from langchain_community.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults


class DuckDuckGo:
    def search(query: str):
        search = DuckDuckGoSearchRun()
        return search.invoke(query)

    def search_results(query: str, keyword: str):
        results = DuckDuckGoSearchResults(backend=keyword)
        return results.invoke(query)
