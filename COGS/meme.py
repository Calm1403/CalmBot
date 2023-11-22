from discord.ext import commands
from colorama import Fore as F
import aiohttp
import discord


class meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"[{F.LIGHTBLUE_EX}COGS{F.RESET}] The meme.py cog has been {F.GREEN}loaded{F.RESET}!"
        )

    @commands.command(aliases=["meme"])
    async def send_meme(self, ctx):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get("https://meme-api.com/gimme") as request:
                    meme_to_be_sent = await request.json()

                await ctx.send(f"{ctx.author.mention}: Here you are! {meme_to_be_sent['url']}")

            except:
                print(
                    f"[{F.YELLOW}API{F.RESET}] {F.RED}Error{F.RESET} with request: {request.status} | {request.url}"
                )
                await ctx.send(f"{ctx.author.mention}: Sorry, there was a problem with the request..")


async def setup(client):
    await client.add_cog(meme(client))
