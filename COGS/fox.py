from discord.ext import commands
from colorama import Fore as F
import aiohttp
import discord


class fox(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"~~~ The fox.py cog has been {F.GREEN}loaded{F.RESET}! ~~~")

    @commands.command(aliases=["fox"])
    async def send_fox(self, ctx):
        # This command will send a picture of a fox.

        async with aiohttp.ClientSession() as session:
            async with session.get("https://randomfox.ca/floof/") as request:
                fox_to_be_sent = await request.json()["image"]

                await ctx.send(f"{ctx.author.mention}: Here you are! {fox_to_be_sent}")


async def setup(client):
    await client.add_cog(fox(client))
