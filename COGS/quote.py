from discord.ext import commands
from colorama import Fore as F
import requests
import discord


class quote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"~~~ The quote.py cog has been {F.GREEN}loaded{F.RESET}! ~~~")

    @commands.command(aliases=["quote"])
    async def send_quote(self, ctx):
        # This command will send a quote.
        request = requests.get("https://quotenjoke.onrender.com/quote")
        quote_to_be_sent = request.json()

        if request.status_code == 500:
            await ctx.send(f"{ctx.author.mention}: Sorry.. there was a problem with the request.")

        else:
            await ctx.send(f"{ctx.author.mention}: \"{quote_to_be_sent['content']}\" - {quote_to_be_sent['author']}")


async def setup(client):
    await client.add_cog(quote(client))
