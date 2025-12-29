from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()
client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
def fetch_market_data(query: str):
    print(f" Searching for {query} on the web...")
    response = client.search(query=query, search_depth='advanced', max_results=5)
    context = ""
    for result in response['results']:
         context += f"\nSource: {result['url']}\nContent: {result['content']}\n"
    return context