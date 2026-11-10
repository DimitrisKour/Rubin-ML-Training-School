# MCP servers for BOOM and ML models

**Tuesday November 10, 2:45–4:00** · Room 401-20 · Leo Conforti

An MCP server gives a language model tools it can call. In this session you use one for BOOM: alert search, light curves, cutouts, cross-matches and similar objects. You try it in the browser and from Python, write the agent loop yourself, and add your own model as a tool.

Everything runs on our own BOOM and Babamul, set up for this session. The site is:

```
https://swaziland-tokyo-cargo-seeking.trycloudflare.com
```

Below, `<site>` means that URL. It is also on the slide and on the paper slips. If the tunnel restarts during the session the URL changes, and the slide will show the new one.

## What to bring

- Your laptop with the `rubin-ml-school` environment from Day 1.
- A way to sign in on the site: your Google account, or the paper slip from your seat, which has an email and a password.
- A Babamul token that starts with `bbml_`, for the notebook and MCP clients. The slip has one. If you sign in with Google, make one on the site: open your account menu, then **Profile**, then **Create New** under **API Tokens**, and copy the token when it appears.

Your Day 1 Babamul token is for babamul.caltech.edu and does not work on our site. Leave it where it is. Nothing in this session changes it or `setup/.env`.

## Material

- [`mcp_servers.ipynb`](mcp_servers.ipynb): call the tools yourself, ask Babamul, write the agent loop, break it, and add your model.
- [`my_model.py`](my_model.py): a plugin for the server, with one working tool (`color_change`) and a commented example for the LUNA pipeline.
- [`.env.example`](.env.example): the settings the notebook reads.

## Setup

1. Pull the latest version of this repository.
2. Optional: in this folder, copy `.env.example` to `.env` and fill in `SESSION_BOOM_URL` and `SESSION_BABAMUL_TOKEN` (the site URL and your token). Git ignores `.env`. If you skip this, the notebook asks.
3. Open `mcp_servers.ipynb` with the `rubin-ml-school` kernel and run the first cell. It installs `mcp` and `boom-mcp` if they are missing. To install them yourself:

   ```bash
   pip install "mcp>=2.3,<3" "git+https://github.com/leonitousconforti/boom-mcp@ae53a96ee6d260b7b29b4e1dc14afe1f5208f01e"
   ```

## Two ways to take part

### The Ask panel

Open `<site>` in a browser, sign in with Google or with the email and password on your slip, and press **Ask** in the header. Nothing to install. Each tool call shows up as a chip you can open.

### Your own MCP client

The MCP server is at `<site>/mcp` (Streamable HTTP). Send your token in the header `Authorization: Bearer bbml_...`.

Claude Code:

```bash
claude mcp add --transport http boom <site>/mcp --header "Authorization: Bearer bbml_..."
```

Claude Desktop needs Node.js and the `mcp-remote` bridge to send the header. Add this to `claude_desktop_config.json` and restart it:

```json
{
  "mcpServers": {
    "boom": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "<site>/mcp", "--header", "Authorization:${BOOM_AUTH}"],
      "env": { "BOOM_AUTH": "Bearer bbml_..." }
    }
  }
}
```

VS Code, Cursor, Gemini CLI and other clients take the same URL and header.

To give your client your own model as well, run boom-mcp locally with your plugin. Use the full path to the Python of the `rubin-ml-school` environment. To find it, run `import sys; print(sys.executable)` in the notebook. In Claude Code:

```bash
claude mcp add boom-local -e BABAMUL_API_URL=<site>/api/babamul -e BABAMUL_API_TOKEN=bbml_... \
  -- /path/to/rubin-ml-school/bin/python -m boom_mcp.server --plugin /full/path/to/my_model.py
```

## Troubleshooting

- **"The site URL should start with https://"**: copy the whole URL, `https://` included. Check that `SESSION_BOOM_URL` is not set to something else in your shell; the environment wins over `.env`.
- **"Babamul rejected the API token"**: you are using your Day 1 token, or the token has a typo. Use the one from your slip or the one you made on your Profile page. The message mentions `BABAMUL_ENV`, which you can ignore here.
- **"Could not reach <site>/mcp", or the site does not load**: check the URL against the slide. If the tunnel restarts, the URL changes. Ask Leo for the new one.
- **"The server stopped answering"**: the tunnel gives up on a request after about 100 seconds. Use a shorter time window or more cuts. If every request fails, ask Leo whether the URL changed.
- **The assistant answers without any tool chips, or makes up results**: in a long conversation it can stop calling tools. Start a new chat and ask again.
- **"Waiting for the model, 3 questions ahead of you"**: the room shares one model, so questions wait in line. If it says the assistant is busy, try again in a few minutes.
- **`No module named 'mcp'` or `'boom_mcp'`**: run the install cell, and check that the kernel is `rubin-ml-school`. If an import fails right after the install, restart the kernel.
- **`cannot import name 'Client' from 'mcp.client'`**: you have an old `mcp` (1.x). Run `pip install -U "mcp>=2.3,<3"` and restart the kernel.
- **Part 3 skips its cells**: it needs `LLM_URL` (an OpenAI-compatible base URL ending in `/v1`), plus `LLM_MODEL` and, if needed, `LLM_API_KEY`. Without them, follow along on the projector.
- **Part 3 says the model server answered 400 about `chat_template_kwargs`**: your server does not take that option. Delete that line in `agent()`.
- **"The local server stopped"** (part 5): the server's traceback is above that message or in the terminal that runs Jupyter. It is usually an error in `my_model.py`.
- **Red `HTTP Request: GET ...` lines in part 5**: that is the local server's log. They are normal.
- **The notebook asks for the URL and nothing seems to happen**: in VS Code the input box is at the top of the window.

The server's code is at [github.com/leonitousconforti/boom-mcp](https://github.com/leonitousconforti/boom-mcp/tree/ae53a96ee6d260b7b29b4e1dc14afe1f5208f01e).
