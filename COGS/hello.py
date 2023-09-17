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
            random_greetings_list = []

            for element in random_greetings_file.readlines():
                if element.__contains__("\n"):
                    random_greetings_list.append(element[:-1])

                else:
                    random_greetings_list.append(element)

            random_greeting = random.choice(random_greetings_list)

        await ctx.send(f"{ctx.author.mention}: {random_greeting}")


async def setup(client):
    await client.add_cog(hello(client))
