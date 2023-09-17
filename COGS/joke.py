from discord.ext import commands
from colorama import Fore as F
import requests
import discord


class joke(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"~~~ The joke.py cog has been {F.GREEN}loaded{F.RESET}! ~~~")

    @commands.command(aliases=["joke"])
    async def send_joke(self, ctx):
        # This command will send a joke.
        request = requests.get("https://quotenjoke.onrender.com/joke")

        if request.status_code == 500:
            await ctx.send(f"{ctx.author.mention}: Sorry.. there was a problem with the request.")

        else:
            joke_to_be_sent = request.json()
            await ctx.send(f"{ctx.author.mention}: {joke_to_be_sent['joke']}")


async def setup(client):
    await client.add_cog(joke(client))
