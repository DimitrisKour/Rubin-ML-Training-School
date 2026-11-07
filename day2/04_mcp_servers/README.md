# MCP servers for BOOM and ML models

**Tuesday November 10, 2:45–4:00** · Room 401-20 · Leo Conforti

This session shows how Model Context Protocol (MCP) servers expose BOOM queries and trained ML models as tools that language-model agents and SkyPortal can call. Participants connect to an MCP server and use it to query alerts and run classification and anomaly models.

## Material

- [`mcp_servers.ipynb`](mcp_servers.ipynb): call the BOOM MCP server's tools yourself, let Claude call them, write the agent loop, and add your own model as a tool.
- [`my_model.py`](my_model.py): a plugin for the server. It has one working tool (`color_change`) and a sketch for wrapping the LUNA pipeline.

## Before the session

1. Install the packages in `requirements.txt` (they include `anthropic`, `mcp` and `boom-mcp`). The notebook also installs them if they are missing.
2. Have your Babamul token in `setup/.env` as `BABAMUL_API_TOKEN`, from the Day 1 setup.
3. Add `ANTHROPIC_API_KEY` to the same file. We hand out a key in the session; don't commit it or paste it anywhere shared.

## Using your own MCP client

If you already use Claude Code, Claude Desktop, VS Code, Cursor or Gemini CLI, you can connect it to the same server: add an HTTP MCP server at `https://boom-mcp.ltgk.net/mcp` with the header `Authorization: Bearer <your Babamul token>`. For example, in Claude Code:

```bash
claude mcp add --transport http boom https://boom-mcp.ltgk.net/mcp --header "Authorization: Bearer $BABAMUL_API_TOKEN"
```

The server code, and the config for other clients, is at [github.com/leonitousconforti/boom-mcp](https://github.com/leonitousconforti/boom-mcp).
