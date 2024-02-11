from discord.ext import commands
from colorama import Fore as F
import aiohttp


class bored(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"[{F.LIGHTBLUE_EX}COGS{F.RESET}] The bored.py cog has been {F.GREEN}loaded{F.RESET}!"
        )

    @commands.command(aliases=["bored"])
    async def boredom(self, ctx):

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get("http://www.boredapi.com/api/activity/") as request:

                    task_to_be_sent = await request.json()

                await ctx.send(
                    f"{ctx.author.mention}: {task_to_be_sent['activity']}! :smile:"
                )

            except Exception as e:
                print(
                    f"[{F.YELLOW}API{F.RESET}] {F.RED}Error{F.RESET} with request: {request.status} | {request.url} | {e}"
                )
                await ctx.send(
                    f"{ctx.author.mention}: Sorry, there was a problem with the request.."
                )


async def setup(client):
    await client.add_cog(bored(client))
