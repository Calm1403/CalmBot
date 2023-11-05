from discord.ext import commands
from colorama import Fore as F
import aiohttp
import discord


class quote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"[{F.LIGHTBLUE_EX}COGS{F.RESET}] The quote.py cog has been {F.GREEN}loaded{F.RESET}!"
        )

    @commands.command(aliases=["quote"])
    async def send_quote(self, ctx):
        # This command will send a quote.

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get("https://quotenjoke.onrender.com/quote") as request:
                    quote_to_be_sent = await request.json()

                await ctx.send(f"{ctx.author.mention}: \"{quote_to_be_sent['content']}\" - {quote_to_be_sent['author']}")

            except:
                print(
                    f"[{F.YELLOW}API{F.RESET}] {F.RED}Error{F.RESET} with request: {request.status} | {request.url}"
                )
                return await ctx.send(f"{ctx.author.mention}: Sorry, there was a problem with the request..")


async def setup(client):
    await client.add_cog(quote(client))
