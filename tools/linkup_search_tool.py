from linkup import LinkupClient
import os
from typing import Optional

class LinkupSearchTool:
    def __init__(self):
        self.client = LinkupClient(api_key=os.getenv("LINKUP_API_KEY"))
        
    def run(self, query: str) -> str:
        """
        Run a search query using Linkup API
        
        Args:
            query (str): The search query to execute
            
        Returns:
            str: The search results as a formatted string
        """
        try:
            response = self.client.search(
                query=query,
                depth="deep",
                output_type="sourcedAnswer"
            )
            
            # Format the response
            formatted_results = []
            
            # Add the main answer if available
            if response.answer:
                formatted_results.append(f"Answer: {response.answer}\n")
            
            # Add sources with their snippets
            if response.sources:
                formatted_results.append("Sources:")
                for source in response.sources:
                    formatted_results.append(f"\n- {source.name}")
                    formatted_results.append(f"  URL: {source.url}")
                    formatted_results.append(f"  Snippet: {source.snippet}\n")
            
            return "\n".join(formatted_results)
            
        except Exception as e:
            return f"Error performing search: {str(e)}"

# Create a singleton instance
linkup_search_tool = LinkupSearchTool() 