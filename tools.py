from langchain_core.tools import tool
from ddgs import DDGS


@tool
def search_tool(query: str) -> str:
    """Search for web information using DuckDuckGo."""
    try:
        ddgs = DDGS()
        results = ddgs.text(query, max_results=5)
        if results:
            formatted_results = "\n".join(
                [f"- {result['title']}: {result['body']}" for result in results]
            )
            return formatted_results
        else:
            return "No results found."
    except Exception as e:
        return f"Search error: {str(e)}"
