from discord.ext import commands
from colorama import Fore as F
import asyncio
import discord
import os

client = commands.Bot(command_prefix="$",
                      intents=discord.Intents.all(), help_command=None)


@client.event
async def on_ready():
    print(
        f"~~~ The CalmBot has {F.GREEN}connected{F.RESET} to discord! ~~~"
    )


@client.event
async def on_message(message):
    # Anti-Rickroll.
    await client.process_commands(message)
    channel = client.get_channel(message.channel.id)

    if message.content == "https://youtu.be/dQw4w9WgXcQ":
        await message.delete()
        await channel.send(f"{message.author.mention}: Nope! No rick-rolling while I'm in town!")


async def load():
    for filename in os.listdir("Python/BOT/COGS"):
        if filename.endswith(".py"):
            await client.load_extension(f"COGS.{filename[:-3]}")


async def main():
    os.system("clear")
    with open("Python/BOT/token.txt") as token:
        token = token.read()

    async with client:
        await load()
        await client.start(token)

asyncio.run(main())
