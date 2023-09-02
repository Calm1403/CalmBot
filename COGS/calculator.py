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
        # This function will, as the name suggests, will act like that of a simple calculator.

        def check(m):
            return m.author == ctx.author

        await ctx.send(f"{ctx.author.mention}: Enter your first number!")
        number_1 = await self.client.wait_for("message", check=check)

        try:
            number_1 = int(number_1.content)
            # If the number the bot recieved can't be converted to an int.

        except:
            await ctx.send(f"{ctx.author.mention}: That's not a number yo.. :skull:")
            # Send output "That's not a number yo.." to chat.
            return
            # Return nothing to stop the bot during an active command.

        await ctx.send(f"{ctx.author.mention}: Enter your operator!")
        operator = await self.client.wait_for("message", check=check)

        if operator.content not in ("*", "/", "+", "-", "%", "^"):
            # If the operand the bot recieved is not in hard-coded tuple.
            await ctx.send(f"{ctx.author.mention}: That's not an operator yo.. :skull:")
            # Send output "That's not an operator yo.." to chat.
            return

        await ctx.send(f"{ctx.author.mention}: Enter your second number!")
        number_2 = await self.client.wait_for("message", check=check)

        try:
            number_2 = int(number_2.content)

        except:
            await ctx.send(f"{ctx.author.mention}: That's not a number yo.. :skull:")
            return

        if operator.content == "*":
            # If the entered operator is equal to astrix.
            output = number_1 * number_2
            # Calculate output.
            await ctx.send(
                f"{ctx.author.mention}: {number_1} * {number_2} = {output}")
            # Send output to display.

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
                f"{ctx.author.mention}: {number_1} ^ {number_2} = {output}"
            )

        else:
            # Else, during the event that the operator the bot recieved is not equal to any of the other operators, but in the hard-coded tuple.
            output = number_1 / number_2
            # Calculate only remaining operator.
            await ctx.send(
                f"{ctx.author.mention}: {number_1} / {number_2} = {output}")
            # Send output to display.


async def setup(client):
    await client.add_cog(calculator(client))
