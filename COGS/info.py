from discord.ext import commands
from colorama import Fore as F
import discord


class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"[{F.LIGHTBLUE_EX}COGS{F.RESET}] The info.py cog has been {F.GREEN}loaded{F.RESET}!"
        )

    @commands.command(aliases=["help"])
    async def info(self, ctx):
        # This command will send info about the bot.

        embeded_message = discord.Embed(
            title="About CalmBot:", description="This message will give you all of the information regarding CalmBot!", colour=discord.Colour.dark_gray())

        embeded_message.set_thumbnail(
            url=self.client.user.avatar.url
        )

        embeded_message.add_field(
            name="$info:", value="[Alias: $help] This asks CalmBot to say their avaliable commands and other information.", inline=False
        )

        embeded_message.add_field(
            name="$hello:", value="[Alias: $hi] This asks CalmBot to say a (most of the time :shrug:) friendly greeting.", inline=False
        )

        embeded_message.add_field(
            name="$eight_ball:", value="[Alias: $8ball] This asks CalmBot to say a yes or no response to a yes or no question.", inline=False
        )

        embeded_message.add_field(
            name="$ping:", value="[Alias: $latency] This asks CalmBot to say their current latency.", inline=False
        )

        embeded_message.add_field(
            name="$calculator:", value="[Alias: $calc] This asks CalmBot to assist you with simple math sums.", inline=False
        )

        embeded_message.add_field(
            name="$roll_dice:", value="[Alias: $dice] This asks CalmBot to play a game of dice.", inline=False
        )

        embeded_message.add_field(
            name="$send_quote:", value="[Alias: $quote] This asks CalmBot to say a quote.", inline=False
        )

        embeded_message.add_field(
            name="$send_joke:", value="[Alias: $joke] This asks CalmBot to tell a joke.", inline=False
        )

        embeded_message.add_field(
            name="$send_fox:", value="[Alias: $fox] This asks CalmBot to display a cute fox.", inline=False
        )

        embeded_message.add_field(
            name="$send_dog:", value="[Aliases: $dog] This asks CalmBot to display a cute dog.", inline=False
        )

        await ctx.send(f"{ctx.author.mention}: Here you are!", embed=embeded_message)


async def setup(client):
    await client.add_cog(info(client))
