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
        pass


async def setup(client):
    await client.add_cog(calculator(client))
