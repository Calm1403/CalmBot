from discord.ext import commands
from colorama import Fore as F
import aiohttp


class fox(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"[{F.LIGHTBLUE_EX}COGS{F.RESET}] The fox.py cog has been {F.GREEN}loaded{F.RESET}!"
        )

    @commands.command(aliases=["fox"])
    async def send_fox(self, ctx):

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                        "https://randomfox.ca/floof/") as request:
                    fox_to_be_sent = await request.json()

                await ctx.send(
                    f"{ctx.author.mention}: Here you are! {fox_to_be_sent['image']}"
                )

            except:
                print(
                    f"[{F.YELLOW}API{F.RESET}] {F.RED}Error{F.RESET} with request: {request.status} | {request.url}"
                )
                await ctx.send(
                    f"{ctx.author.mention}: Sorry, there was a problem with the request.."
                )


async def setup(client):
    await client.add_cog(fox(client))
