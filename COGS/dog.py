from discord.ext import commands
from colorama import Fore as F
import requests
import discord


class dog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("~~~ The dog.py cog has been")

    @commands.command(aliases=["dog"])
    async def send_dog(self, ctx):
        request = requests.get("https://dog.ceo/api/breeds/image/random")
        dog_to_be_sent = request.json()["message"]

        await ctx.send(f"{ctx.author.mention}: Here you are! {dog_to_be_sent}")


async def setup(client):
    await client.add_cog(dog(client))
