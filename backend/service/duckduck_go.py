from langchain_community.tools import DuckDuckGoSearchRun

class DuckDuckGo:
    def search(query: str) -> str:
        search = DuckDuckGoSearchRun()
        return search.run(query)
