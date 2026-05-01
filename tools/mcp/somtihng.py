import asyncio
from .client import call_mcp

def something_tool(something: str, number: str) -> str:
    params = {"something": something, "number": number}
    return asyncio.run(
        call_mcp("something", params, server_url="http://localhost:8000/sse")
    )