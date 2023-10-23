from discord.ext import commands
from colorama import Fore as F
import discord
import random


class hello(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"~~~ The hello.py cog has been {F.GREEN}loaded{F.RESET}! ~~~")

    @commands.command(aliases=["hi"])
    # This decorator will intake a function to be used as a discord command.
    async def hello(self, ctx):
        # This command will display a friendly greeting.
        with open("Python/BOT/COGS/greetings.txt") as random_greetings_file:
            random_greeting = random.choice(random_greetings_file.readlines())

            if random_greeting.__contains__("\n"):
                await ctx.send(f"{ctx.author.mention}: {random_greeting[:-1]}")
                return

            await ctx.send(f"{ctx.author.mention}: {random_greeting}")


async def setup(client):
    await client.add_cog(hello(client))
