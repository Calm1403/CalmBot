from discord.ext import commands
from colorama import Fore as F
import aiohttp
import discord


class joke(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"[{F.LIGHTBLUE_EX}COGS{F.RESET}] The joke.py cog has been {F.GREEN}loaded{F.RESET}!"
        )

    @commands.command(aliases=["joke"])
    async def send_joke(self, ctx):
        # This command will send a joke.

        async with aiohttp.ClientSession() as session:
            async with session.get("https://quotenjoke.onrender.com/joke") as request:
                if request.status != 200:
                    return await ctx.send(f"{ctx.author.mention}: Sorry, there was a problem with the request.. {request.status}")

                joke_to_be_sent = await request.json()

            await ctx.send(f"{ctx.author.mention}: {joke_to_be_sent['joke']}")


async def setup(client):
    await client.add_cog(joke(client))
