from discord.ext import commands
from colorama import Fore as F
import asyncio
import discord
import os

client = commands.Bot(command_prefix="$",
                      intents=discord.Intents.all(),
                      help_command=None)


@client.event
async def on_ready():
    os.system("clear")

    print(
        f"[{F.LIGHTMAGENTA_EX}BOT{F.RESET}] The CalmBot has {F.GREEN}connected{F.RESET} to discord!"
    )

    print("""
 ██████╗ █████╗ ██╗     ███╗   ███╗    ██████╗  ██████╗ ████████╗
██╔════╝██╔══██╗██║     ████╗ ████║    ██╔══██╗██╔═══██╗╚══██╔══╝
██║     ███████║██║     ██╔████╔██║    ██████╔╝██║   ██║   ██║   
██║     ██╔══██║██║     ██║╚██╔╝██║    ██╔══██╗██║   ██║   ██║   
╚██████╗██║  ██║███████╗██║ ╚═╝ ██║    ██████╔╝╚██████╔╝   ██║   
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝    ╚═════╝  ╚═════╝    ╚═╝
 """)


async def load():
    for filename in os.listdir("Python/BOT/COGS"):
        if filename.endswith(".py"):
            await client.load_extension(f"COGS.{filename[:-3]}")


async def main():
    with open("Python/BOT/token.txt") as token:
        token = token.read()

    async with client:
        await load()
        await client.start(token)


try:
    asyncio.run(main())

except KeyboardInterrupt:
    os.system("clear")

    print(
        f"[{F.LIGHTMAGENTA_EX}BOT{F.RESET}] The CalmBot has been {F.RED}shutdown{F.RESET}!"
    )
