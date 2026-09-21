# Pingo

A simple Discord bot that automatically pings a specified role in multiple text channels.

The bot also includes a `/ping` command that displays its current Discord latency and a small Flask web server for keeping the bot online on hosting services that require an HTTP endpoint.

## Features

* Automatically pings a configured Discord role in `pings*` channels.
* Scans for matching channels every second.
* `/ping` command for checking bot latency.
* Flask keep-alive endpoint at `/`.
* Configuration stored locally in `config.json`.

## Requirements

* Python 3.10+
* A Discord bot account
* A Discord server where the bot has permission to send messages and mention the configured role

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `config.json` file in the project directory:

```json
{
    "spam_guild_id": "YOUR_GUILD_ID",
    "ping_role_id": "YOUR_ROLE_ID",
    "bot_token": "YOUR_BOT_TOKEN"
}
```

Replace the values with your Discord server ID, role ID, and bot token.

## Running

Start the bot with:

```bash
python bot.py
```

Once connected, the bot will automatically begin checking for channels starting with `pings`.

The default channel-name check is:

```python
channel.name.startswith("pings")
```

You can change `"pings"` in `bot.py` to use a different channel prefix.

## `/ping`

Use:

```text
/ping
```

The bot will respond with its current WebSocket latency in milliseconds.

## Keep Alive

`keep_alive.py` starts a Flask server on port `8080` with a simple status page:

```text
Bot is online.
```

The endpoint is available at `/`.

**Never upload `config.json` to GitHub.**

Your Discord bot token is a secret. If it is ever exposed publicly or committed to GitHub, regenerate the token through the Discord Developer Portal.

## Files

```text
├── bot.py
├── keep_alive.py
├── requirements.txt
├── config.json
└── README.md
```

`config.json` should remain local and should not be committed to the repository.
