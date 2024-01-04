from discord.ext import commands
from colorama import Fore as F
import asyncio


class calculator(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"[{F.LIGHTBLUE_EX}COGS{F.RESET}] The calculator.py cog has been {F.GREEN}loaded{F.RESET}!"
        )

    @commands.command(aliases=["calc"])
    async def calculator(self, ctx):

        def check(m):
            return m.author == ctx.author

        await ctx.send(f"{ctx.author.mention}: Enter your first number!")

        try:
            number_1 = await self.client.wait_for("message",
                                                  check=check,
                                                  timeout=10.0)

        except asyncio.TimeoutError:
            return await ctx.send(
                f"{ctx.author.mention}: Fine.. don't enter your first number. :unamused:"
            )

        try:
            number_1 = int(number_1.content)

        except:
            return await ctx.send(
                f"{ctx.author.mention}: That's not a number yo.. :skull:")

        await ctx.send(f"{ctx.author.mention}: Enter your operator!")

        try:
            operator = await self.client.wait_for("message",
                                                  check=check,
                                                  timeout=10.0)

        except asyncio.TimeoutError:
            return await ctx.send(
                f"{ctx.author.mention}: Fine.. don't enter your operator. :unamused:"
            )

        if operator.content not in ("*", "/", "+", "-", "%", "^"):
            return await ctx.send(
                f"{ctx.author.mention}: That's not an operator yo.. :skull:")

        await ctx.send(f"{ctx.author.mention}: Enter your second number!")

        try:
            number_2 = await self.client.wait_for("message",
                                                  check=check,
                                                  timeout=10.0)

        except asyncio.TimeoutError:
            return await ctx.send(
                f"{ctx.author.mention}: Fine.. don't enter your second number. :unamused:"
            )

        try:
            number_2 = int(number_2.content)

        except:
            return await ctx.send(
                f"{ctx.author.mention}: That's not a number yo.. :skull:")

        if operator.content == "*":
            output = number_1 * number_2
            return await ctx.send(
                f"{ctx.author.mention}: {number_1} * {number_2} = {output}")

        if operator.content == "+":
            output = number_1 + number_2
            return await ctx.send(
                f"{ctx.author.mention}: {number_1} + {number_2} = {output}")

        if operator.content == "-":
            output = number_1 - number_2
            return await ctx.send(
                f"{ctx.author.mention}: {number_1} - {number_2} = {output}")

        if operator.content == "%":
            output = number_1 % number_2
            return await ctx.send(
                f"{ctx.author.mention}: {number_1} % {number_2} = {output}")

        if operator.content == "^":
            output = number_1 ^ number_2
            return await ctx.send(
                f"{ctx.author.mention}: {number_1} ^ {number_2} = {output}")

        try:
            output = number_1 / number_2

        except:
            return await ctx.send(
                f"{ctx.author.mention}: I can't really divide {number_1} by {number_2} can I now?"
            )

        await ctx.send(
            f"{ctx.author.mention}: {number_1} / {number_2} = {output}")


async def setup(client):
    await client.add_cog(calculator(client))
