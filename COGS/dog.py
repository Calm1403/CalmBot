from discord.ext import commands
from colorama import Fore as F
import aiohttp
import discord


class dog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"[{F.LIGHTBLUE_EX}COGS{F.RESET}] The dog.py cog has been {F.GREEN}loaded{F.RESET}!"
        )

    @commands.command(aliases=["dog"])
    async def send_dog(self, ctx):
        # This command will send a picture of a dog.
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dog.ceo/api/breeds/image/random") as request:
                if request.status != 200:
                    return await ctx.send(f"{ctx.author.mention}: Sorry, there was a problem with the request.. {request.status}")

                dog_to_be_sent = await request.json()

            await ctx.send(f"{ctx.author.mention}: Here you are! {dog_to_be_sent['message']}")


async def setup(client):
    await client.add_cog(dog(client))
