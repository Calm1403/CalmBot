from discord.ext import commands
from colorama import Fore as F
import random


class hello(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"[{F.LIGHTBLUE_EX}COGS{F.RESET}] The hello.py cog has been {F.GREEN}loaded{F.RESET}!"
        )

    @commands.command(aliases=["hi"])
    async def hello(self, ctx):
        with open("Python/BOT/COGS/greetings.txt") as random_greetings_file:
            random_greeting = random.choice(random_greetings_file.readlines())

        if random_greeting[len(random_greeting) - 1] == "\n":
            return await ctx.send(
                f"{ctx.author.mention}: {random_greeting[:-1]}")

        await ctx.send(f"{ctx.author.mention}: {random_greeting}")


async def setup(client):
    await client.add_cog(hello(client))
