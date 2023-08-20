from discord.ext import commands, tasks
from colorama import Fore as F
from itertools import cycle
import discord
import random
import os

client = commands.Bot(command_prefix="$",
                      intents=discord.Intents.all(), help_command=None)


client_status = cycle(
    [
        "Fallout 4",
        "Team Fortress 2",
        "Visual Studio Code",
        "Minecraft",
        "Warframe"
    ]
)


# The cycle class creates a generator, which unlike that of an itterator, holds only one value at a
# time until called upon again with the next() function, at which point will then hold the next value.


# NOTE:

# Discord likes to use asyncronous functions for making discord bots with python
# because asyncronous functions provide the ability to allow functions to be exicuted
# during the time another function is idle or currently doing something, not to be mistaken
# for something like multithreading that allows functions to occure at the exact same time, which is
# really CPU intensive; asyncrounous is not and only allows functions to occure like that of the
# previously discussed methodology: the ability to occure during idle/proccessing time.


@tasks.loop(seconds=5)
# This decorator will intake a function to be repeated again after a certain ammount of time has passed.
async def change_status():
    await client.change_presence(activity=discord.Game(next(client_status)))


@client.event
# This decorator will intake an event function to be exicuted during a specific event specified by the name of the function passed through it.
async def on_ready():
    change_status.start()
    # This begins the bot's status cycle process.

    print(
        f"\n~~~ The CalmBot has become {F.GREEN}fully{F.RESET} active! ~~~\n")


@client.event
async def on_message(message):
    # Anti-Rickroll.
    await client.process_commands(message)
    channel = client.get_channel(message.channel.id)

    if message.content == "https://youtu.be/dQw4w9WgXcQ":
        await message.delete()
        await channel.send(f"{message.author.mention}: Nope! No rick-rolling while I'm in town!")


@client.command(aliases=["calc"])
async def calculator(ctx):

    await ctx.send(f"{ctx.author.mention}: Enter your first number!")
    number_1 = await client.wait_for("message")

    try:
        number_1 = int(number_1.content)
    except:
        await ctx.send(f"{ctx.author.mention}: That's not a number yo..")
        return

    await ctx.send(f"{ctx.author.mention}: Enter your operator!")
    operator = await client.wait_for("message")

    if operator.content not in ("*", "/", "+", "-"):
        await ctx.send(f"{ctx.author.mention}: That's not an operator yo..")
        return

    await ctx.send(f"{ctx.author.mention}: Enter your second number!")
    number_2 = await client.wait_for("message")

    try:
        number_2 = int(number_2.content)
    except:
        await ctx.send(f"{ctx.author.mention}: That's not a number yo..")
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

    else:
        output = number_1 / number_2
        await ctx.send(
            f"{ctx.author.mention}: {number_1} / {number_2} = {output}")


@client.command(aliases=["help"])
async def info(ctx):
    embeded_message = discord.Embed(
        title="About CalmBot:", description="This message will tell you the information regarding CalmBot.", colour=discord.Colour.dark_gray())

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

    await ctx.send(embed=embeded_message)


@client.command(aliases=["hi"])
# This decorator will intake a function to be used as a discord command.
# The parameter aliases intakes a list of strings to be used as ways of calling the command function.
async def hello(ctx):
    # The ctx perameter referes to the context of the conversation between
    # the person calling the bot and the bot itself and is always required.
    with open("Python/BOT/greetings.txt") as random_greetings_file:
        random_greetings_list = []

        for element in random_greetings_file.readlines():
            # For every element in the readlines() object:
            if element.__contains__("\n"):
                # If that element contains \n:
                random_greetings_list.append(element[:-1])
                # Append new element to random_greetings_list.

            else:
                # If not, append element.
                random_greetings_list.append(element)

        random_greeting = random.choice(random_greetings_list)

    await ctx.send(f"{ctx.author.mention}: {random_greeting}")


@client.command(alias=["latency"])
async def ping(ctx):
    await ctx.send(f"{ctx.author.mention}: My latency is {int(client.latency * 1000)}ms.")


@client.command(aliases=["8ball"])
async def eight_ball(ctx):

    # NOTE:
    # The question parameter for commands referes to a question
    # passed through the command and is in string format; I don't use it here, thus mentioning it to remember it.
    # The astrix is used by discord to include all following words as the question.
    # I'm not too sure what discord does with the astrix, but I do know it's used to instantiate a key
    # arguments parameter and unpack lists in other cases.

    with open("Python/BOT/responses.txt") as random_responses_file:
        random_responses_list = []

        for element in random_responses_file.readlines():
            if element.__contains__("\n"):
                random_responses_list.append(element[:-1])

            else:
                random_responses_list.append(element)

        random_response = random.choice(random_responses_list)

    await ctx.send(f"{ctx.author.mention}: {random_response}")


with open("Python/BOT/token.txt") as file:
    os.system("clear")
    # This reads the file containing the discord bot's token.
    # The log_handler perameter prevents the discord bot from logging
    # to terminal by its self allowing me to add custom logging.

    client.run(file.read())

# NOTE:

# My Sister harriet helped me with some spelling, so she.. "deserves" some credit.

# TODO:

# Get around to cogs harris ya lazy (*word that should not be said, nor have been created by man here*)!
