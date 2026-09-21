import discord
from discord.ext import commands
import asyncio
import json
from keep_alive import keep_alive

intents = discord.Intents.default()

pingo = commands.Bot(
    command_prefix="_",
    help_command=None,
    intents=intents
)

with open("config.json", "r") as f:
    file = json.load(f)

guildid = int(file["spam_guild_id"])
roleid = file["ping_role_id"]
bottoken = file["bot_token"]

ping_task_running = False


async def ping_task():
    global ping_task_running

    if ping_task_running:
        return

    ping_task_running = True

    while True:
        guild = pingo.get_guild(guildid)

        if guild is not None:
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    if channel.name.startswith("pingss"):
                        try:
                            await channel.send(f"<@&{roleid}>")
                        except discord.HTTPException as e:
                            print(f"Failed to send in #{channel.name}: {e}")

        await asyncio.sleep(1)


@pingo.event
async def on_ready():
    print(f"Logged in as {pingo.user}")
    asyncio.create_task(ping_task())


@pingo.slash_command(guild_ids=[guildid])
async def ping(ctx):
    await ctx.respond(f"{round(pingo.latency * 1000)}ms")


keep_alive()
pingo.run(bottoken)
