
import asyncio
import sys
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command=sys.executable,
        args=["-u", os.path.abspath("mcp_server.py")],
        env=os.environ.copy()
    )

    print("Starting MCP client...", flush=True)

    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:

                print("Initializing...", flush=True)
                await session.initialize()

                print("MCP Connection Successful!", flush=True)
                print("Requesting available tools...", flush=True)

                tools = await asyncio.wait_for(
                    session.list_tools(),
                    timeout=15
                )

                print("\nAvailable Tools:", flush=True)

                for tool in tools.tools:
                    print("-", tool.name, flush=True)

    except asyncio.TimeoutError:
        print("ERROR: Tool listing timed out after 15 seconds.")

    except Exception as e:
        print("ERROR:", repr(e))


if __name__ == "__main__":
    asyncio.run(main())
