from discord.ext import commands
from colorama import Fore as F
import requests
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
        request = requests.get("https://randomfox.ca/floof/")
        fox_to_be_sent = request.json()["image"]

        await ctx.send(f"{ctx.author.mention}: Here you are! {fox_to_be_sent}")


async def setup(client):
    await client.add_cog(fox(client))
