from discord.ext import commands
from colorama import Fore as F
import discord
import random


class eight_ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"~~~ The eight_ball.py cog has been {F.GREEN}loaded{F.RESET}! ~~~"
        )

    @commands.command(aliases=["8ball"])
    async def eight_ball(self, ctx):
        # This function will display a random response to a question.

        # NOTE:

        # The question parameter for commands referes to a question
        # passed through the command and is in string format; I don't use it here, thus mentioning it to remember it.
        # When the astrix symbol is passed through a command that recieves a question it tells discord include all following words as the question.
        # I'm not too sure what discord does with the astrix, but I do know it's used to instantiate a key
        # arguments parameter and unpack lists in other cases.

        def check(m):
            return m.author == ctx.author

        await ctx.send(f"{ctx.author.mention}: Hey, ask me a yes or no question!")
        question = await self.client.wait_for("message", check=check)

        with open("Python/BOT/COGS/responses.txt") as random_responses_file:
            random_responses_list = []

            for element in random_responses_file.readlines():
                if element.__contains__("\n"):
                    random_responses_list.append(element[:-1])

                else:
                    random_responses_list.append(element)

            random_response = random.choice(random_responses_list)

        await ctx.send(f"{ctx.author.mention}: \"{question.content}\" -- {random_response}")


async def setup(client):
    await client.add_cog(eight_ball(client))
