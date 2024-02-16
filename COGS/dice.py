from discord.ext import commands
from colorama import Fore as F
import asyncio
import random


class dice(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"[{F.LIGHTBLUE_EX}COGS{F.RESET}] The dice.py cog has been {F.GREEN}loaded{F.RESET}!"
        )

    @commands.command(aliases=["dice"])
    async def roll_dice(self, ctx):
        integer_to_guess = random.randint(1, 6)

        def check(m):
            return m.author == ctx.author

        await ctx.send(
            f"{ctx.author.mention}: Alright, I'm gonna roll the dice; bet a number between one and six! :smile:"
        )

        try:
            guess = await self.client.wait_for("message",
                                               check=check,
                                               timeout=10.0)

        except asyncio.TimeoutError:
            return await ctx.send(
                f"{ctx.author.mention}: Why did you ask to play a game of dice if you weren't going to play? :unamused:"
            )

        try:
            guess = int(guess.content)

        except TypeError:
            return await ctx.send(
                f"{ctx.author.mention}: That's not a number yo.. :skull:")

        if guess == integer_to_guess:
            return await ctx.send(
                f"{ctx.author.mention}: You win! The dice landed on {guess}!")

        if guess > 6:
            return await ctx.send(
                f"{ctx.author.mention}: It's a six sided die.. :skull:")

        if guess < 1:
            return await ctx.send(
                f"{ctx.author.mention}: But it can't.. it can't.. what? :skull:"
            )

        await ctx.send(
            f"{ctx.author.mention}: You lose! The dice landed on {integer_to_guess}!"
        )


async def setup(client):
    await client.add_cog(dice(client))
