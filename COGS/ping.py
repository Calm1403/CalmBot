from discord.ext import commands
from colorama import Fore as F
import discord


class ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"[{F.LIGHTBLUE_EX}COGS{F.RESET}] The ping.py cog has been {F.GREEN}loaded{F.RESET}!"
        )

    @commands.command(aliases=["latency"])
    async def ping(self, ctx):
        # This command will get the discord bot's latency.
        await ctx.send(f"{ctx.author.mention}: My latency is {int(self.client.latency * 1000)}ms.")


async def setup(client):
    await client.add_cog(ping(client))
