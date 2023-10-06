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
        # This command will intake a question, then reply to that question with a random response.
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

        await ctx.send(f"{ctx.author.mention}: \"{question.content}\" - {random_response}")


async def setup(client):
    await client.add_cog(eight_ball(client))
