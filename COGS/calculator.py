from discord.ext import commands
from colorama import Fore as F
import discord


class calculator(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"~~~ The calculator.py cog has been {F.GREEN}loaded{F.RESET}! ~~~"
        )

    @commands.command(aliases=["calc"])
    async def calculator(self, ctx):
        # This command will act like that of a simple calculator.
        def check(m):
            return m.author == ctx.author and m[0] != "$"

        await ctx.send(f"{ctx.author.mention}: Enter your first number!")
        number_1 = await self.client.wait_for("message", check=check)

        try:
            number_1 = int(number_1.content)

        except:
            await ctx.send(f"{ctx.author.mention}: That's not a number yo.. :skull:")
            return

        await ctx.send(f"{ctx.author.mention}: Enter your operator!")
        operator = await self.client.wait_for("message", check=check)

        if operator.content not in ("*", "/", "+", "-", "%", "^"):
            await ctx.send(f"{ctx.author.mention}: That's not an operator yo.. :skull:")
            return

        await ctx.send(f"{ctx.author.mention}: Enter your second number!")
        number_2 = await self.client.wait_for("message", check=check)

        try:
            number_2 = int(number_2.content)

        except:
            await ctx.send(f"{ctx.author.mention}: That's not a number yo.. :skull:")
            return

        if operator.content == "*":
            output = number_1 * number_2
            await ctx.send(
                f"{ctx.author.mention}: {number_1} * {number_2} = {output}")

        elif operator.content == "+":
            output = number_1 + number_2
            await ctx.send(
                f"{ctx.author.mention}: {number_1} + {number_2} = {output}")

        elif operator.content == "-":
            output = number_1 - number_2
            await ctx.send(
                f"{ctx.author.mention}: {number_1} - {number_2} = {output}")

        elif operator.content == "%":
            output = number_1 % number_2
            await ctx.send(
                f"{ctx.author.mention}: {number_1} % {number_2} = {output}")

        elif operator.content == "^":
            output = number_1 ^ number_2
            await ctx.send(
                f"{ctx.author.mention}: {number_1} ^ {number_2} = {output}")

        else:
            output = number_1 / number_2
            await ctx.send(
                f"{ctx.author.mention}: {number_1} / {number_2} = {output}")


async def setup(client):
    await client.add_cog(calculator(client))
