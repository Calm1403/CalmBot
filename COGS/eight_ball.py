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

        # Sometimes in command functions, the question parameter for commands can be set and referes to a question
        # passed through the command and is in string format; I don't use it here, thus mentioning it to remember it.
        # When the astrix symbol is passed through a command that recieves a question it tells discord include all following words as the input question.
        # I'm not too sure what discord does with the astrix, but I do know it's used to instantiate a key
        # arguments parameter and unpack lists in other cases.

        def check(m):
            return m.author == ctx.author

        await ctx.send(f"{ctx.author.mention}: Hey, ask me a yes or no question!")
        question = await self.client.wait_for("message", check=check)
        # This makes the bot wait for a user input, then asigns that user input to a variable.

        with open("Python/BOT/COGS/responses.txt") as random_responses_file:
            # This opens the file called responses.txt, and sets the file object to the random_responses_file variable.
            random_responses_list = []
            # This is the array of trimmed elements from the file object.

            for element in random_responses_file.readlines():
                # For each element in the file object.
                if element.__contains__("\n"):
                    # If the current element contains a new line keyword.
                    random_responses_list.append(element[:-1])
                    # Remove the character at the end of the element and append it to the random_response array.

                else:
                    # If the element doesn't contain a new line keyword.
                    random_responses_list.append(element)
                    # Append the element without the \n to be included in the random reponses.

            random_response = random.choice(random_responses_list)
            # Randomly choose one of the elements from the random_responses_list array.

        await ctx.send(f"{ctx.author.mention}: \"{question.content}\", {random_response}")
        # Send that to the discord chat.


async def setup(client):
    await client.add_cog(eight_ball(client))
