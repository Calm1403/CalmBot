from discord.ext import commands
from colorama import Fore as F
import asyncio
import discord
import os

client = commands.Bot(command_prefix="$",
                      intents=discord.Intents.all(), help_command=None)


@client.event
# This decorator will intake a function to be exicuted during a specific event corrosponding to the name of the function it intakes.
async def on_ready():
    # On discord bot ready
    print(
        f"~~~ The CalmBot has {F.GREEN}connected{F.RESET} to discord! ~~~"
    )


@client.event
async def on_message(message):
    # Anti-Rickroll.
    await client.process_commands(message)
    # Check to see if message is a command.

    channel = await client.get_channel(message.channel.id)
    # Get channel identity.

    if message.content == "https://youtu.be/dQw4w9WgXcQ":
        # If message content is equal to rick astley's epic hit music video.
        await message.delete()
        # Delete message.
        await channel.send(f"{message.author.mention}: Nope! No rick-rolling while I'm in town!")
        # Send response to message.


async def load():
    for filename in os.listdir("Python/BOT/COGS"):
        # For every file in the directory.
        if filename.endswith(".py"):
            # If current file in loop ends with .py:
            await client.load_extension(f"COGS.{filename[:-3]}")
            # Remove three characters off of the filename variable and read cog file.


async def main():
    with open("Python/BOT/token.txt") as token:
        # Open token file.
        token = token.read()
        # Read file.

    async with client:
        # Instanciate load function, loading the various cogs.
        await load()
        # Start discord bot using token variable containing the discord bot's token.
        await client.start(token)

asyncio.run(main())
# Run the main function asyncronously.
