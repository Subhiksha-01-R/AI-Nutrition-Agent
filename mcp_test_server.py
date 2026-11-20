
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Test Server")

@mcp.tool()
def hello(name: str) -> str:
    """Return a greeting."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
