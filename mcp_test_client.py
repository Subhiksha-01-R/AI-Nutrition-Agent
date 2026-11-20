
import asyncio
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_mcp():

    params = StdioServerParameters(
        command=sys.executable,
        args=["-u", "mcp_test_server.py"]
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:

            await session.initialize()
            print("Connection successful!", flush=True)

            print("Requesting tools...", flush=True)

            tools = await asyncio.wait_for(
                session.list_tools(),
                timeout=10
            )

            print("Available tools:", flush=True)

            for tool in tools.tools:
                print("-", tool.name, flush=True)

if __name__ == "__main__":
    asyncio.run(test_mcp())
