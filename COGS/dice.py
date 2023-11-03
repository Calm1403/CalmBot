from discord.ext import commands
from colorama import Fore as F
import discord
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
        # This command will ask the user for a number
        # between one and six, generate a random number, and
        # evalutate whether or not the number guessed is equal to the
        # number generated.
        integer_to_guess = random.randint(1, 6)

        def check(m):
            return m.author == ctx.author

        await ctx.send(f"{ctx.author.mention}: Alright, I'm gonna roll the dice; guess a number between one and six! :smile:")
        guess = await self.client.wait_for("message", check=check)

        try:
            guess = int(guess.content)

        except:
            return await ctx.send(f"{ctx.author.mention}: That's not a number yo.. :skull:")

        if guess == integer_to_guess:
            return await ctx.send(f"{ctx.author.mention}: Correct! {guess} was the right answer!")

        if guess > 6:
            return await ctx.send(f"{ctx.author.mention}: This is a six sidded die.. :skull:")

        if guess < 1:
            return await ctx.send(f"{ctx.author.mention}: It.. it doesn't.. what? :skull:")

        if guess != interger_to_guess:
            return await ctx.send(f"{ctx.author.mention}: Nope! {guess} was not the right answer; the right answer was {interger_to_guess}!")


async def setup(client):
    await client.add_cog(dice(client))
