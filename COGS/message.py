from discord.ext import commands
from colorama import Fore as F
import discord


class message(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"~~~ The message.py cog has been {F.GREEN}loaded{F.RESET}!")

    @commands.Cog.listener("on_message")
    async def remove_message(self, message):
        if message.content == "https://youtu.be/dQw4w9WgXcQ":
            await message.delete()
            await message.channel.send(f"{message.author.mention}: Nope! No rick-rolling while I'm in town!")


async def setup(client):
    await client.add_cog(message(client))
