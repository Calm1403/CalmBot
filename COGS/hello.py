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
    # The parameter aliases intakes a list of strings to be used as ways of calling the command function.
    async def hello(self, ctx):
        # This command will display a friendly greeting.
        # The ctx perameter referes to the context of the conversation between
        # the person instanciating the bot command and the bot itself and is always required in a command function.
        with open("Python/BOT/COGS/greetings.txt") as random_greetings_file:
            random_greetings_list = []

            for element in random_greetings_file.readlines():
                # For every element in the readlines() object.
                if element.__contains__("\n"):
                    # If that element contains \n.
                    random_greetings_list.append(element[:-1])
                    # Append new element to random_greetings_list.

                else:
                    random_greetings_list.append(element)
                    # If not, append element.

            random_greeting = random.choice(random_greetings_list)
            # Pick a random response to be sent.

        await ctx.send(f"{ctx.author.mention}: {random_greeting}")
        # Send that randomly chosen response.


async def setup(client):
    await client.add_cog(hello(client))
