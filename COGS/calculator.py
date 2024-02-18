from discord.ext import commands
from colorama import Fore as F
import string
import asyncio

EOF, NONE, OPPERATOR, LITTERAL = "EOF", "NONE", "OPPERATOR", "LITTERAL"


class token(object):
    def __init__(self, type, data):
        self.type = type
        self.data = data


class tokeniser(object):
    potentuals = ("%", "^", "+", "/", "*", "-")

    def __init__(self, text):
        if text > 3:
            # I'll catch this and display the output.
            raise Exception("That expression is too long.. keep it to around three characters please.")

        self.text = text
        self.current_pos = 0
        self.current_token = token(NONE, NONE)

    def get_next_token(self):
        if self.current_pos > len(self.text) - 1:
            return token(EOF, NONE)

        current_char = self.text[self.current_pos]

        if current_char in string.digits:
            self.current_pos += 1
            return token(LITTERAL, current_char)

        if current_char in tokeniser.potentuals:
            self.current_pos += 1
            return token(OPPERATOR, current_char)

        raise Exception(f"I don't think {current_char} is a valid term in an expression..")

    def move_and_assert_type(self, spes_type):
        if self.current_token.type == spes_type:
            self.current_token = self.get_next_token()

        raise Exception(f"I'm not sure if {self.text} is a valid way of constructing an expression.. keep it to something like \"3+3\" please.")

    def calculation(self):
        self.move_and_assert_type(NONE, NONE)

        left = self.current_token
        self.move_and_assert_type(LITTERAL)

        middle = self.current_token
        self.move_and_assert_type(OPPERATOR)

        right = self.current_token
        self.move_and_assert_type(LITTERAL)

        if middle == "+":
            return f"The answer to \"{self.text}\" is {left + right}"

        if middle == "-":
            return f"The answer to \"{self.text}\" is {left - right}"

        if middle == "/":
            return f"The answer to \"{self.text}\" is {left / right}"

        if middle == "^":
            return f"The answer to \"{self.text}\" is {left ^ right}"

        if middle == "%":
            return f"The answer to \"{self.text}\" is {left % right}"

        return f"The answer to \"{self.text}\" is {left * right}"


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
        ctx.send(f"{ctx.author.mention}: Hey! Give me an expression!")


async def setup(client):
    await client.add_cog(calculator(client))
