from discord.ext import commands
from colorama import Fore as F
import discord


class message(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"[{F.LIGHTBLUE_EX}COGS{F.RESET}] The message.py cog has been {F.GREEN}loaded{F.RESET}!"
        )

    @commands.Cog.listener("on_message")
    # This decorator will intake a function to be called during a certain event. In this case it's the on_message event.
    async def remove_message(self, message):
        if message.content == "https://youtu.be/dQw4w9WgXcQ":
            await message.delete()
            await message.channel.send(f"{message.author.mention}: Nope! No rick-rolling while I'm in town!")


async def setup(client):
    await client.add_cog(message(client))
