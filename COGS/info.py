from discord.ext import commands
from colorama import Fore as F
import discord


class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"~~~ The info.py cog has been {F.GREEN}loaded{F.RESET}! ~~~")

    @commands.command(aliases=["help"])
    async def info(self, ctx):
        # This command will display the information regarding the discord bot.

        embeded_message = discord.Embed(
            title="About CalmBot:", description="This message will give you all of the information regarding CalmBot!", colour=discord.Colour.dark_gray())

        embeded_message.set_thumbnail(
            url=ctx.guild.icon
        )

        embeded_message.add_field(
            name="$info:", value="[Alias: $help] This asks CalmBot to say their avaliable commands and other information."
        )

        embeded_message.add_field(
            name="$hello:", value="[Alias: $hi] This asks CalmBot to say a (most of the time :shrug:) friendly greeting."
        )

        embeded_message.add_field(
            name="$eight_ball:", value="[Alias: $8ball] This asks CalmBot to say a yes or no response to a yes or no question."
        )

        embeded_message.add_field(
            name="$ping:", value="[Alias: $latency] This asks CalmBot to say their current latency."
        )

        embeded_message.add_field(
            name="$calculator:", value="[Alias: $calc] This asks CalmBot to assist you with simple math sums."
        )

        embeded_message.add_field(
            name="$pokemon:", value="[Alias: $poke] This asks CalmBot to use the pokeAPI to provide you with information about a specific pokemon."
        )

        await ctx.send(ctx.author.mention, embed=embeded_message)


async def setup(client):
    await client.add_cog(info(client))
