from mcp.server.fastmcp import FastMCP
import httpx
from shared.config import Config

mcp = FastMCP("weather-server", host="0.0.0.0", port=8000)

@mcp.tool()
async def weather(something: str, number: str) -> str:
    """
    function for getting the something from the registry
    """
    try:
        async with httpx.AsyncClient() as client:
            endpoint = f"{Config.Something.URL}/something"
            params = {"something": something, "number": number}
            params = {k: v for k, v in params.items() if v is not None}
            r = await client.get(endpoint, params=params)
        data = r.json()
        if isinstance(data, dict) and "error" in data:
            return f"Error fetching {something}: {data['error']}"

        return str({"something": something, "data": data})
    except Exception as e:
        return f"Error getting weather: {e}"