from langchain_mcp_adapters.client import MultiServerMCPClient


async def flight_search() -> any: 
    client = MultiServerMCPClient(
        {
            "travel_server": {
                "transport": "streamable_http",
                "url": "https://mcp.kiwi.com"
            }
        }
    )
    
    tools = await client.get_tools()