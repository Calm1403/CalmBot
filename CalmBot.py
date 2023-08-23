from discord.ext import commands, tasks
from colorama import Fore as F
from itertools import cycle
import requests
import discord
import random
import json
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
        f"\n~~~ The CalmBot has become {F.GREEN}fully{F.RESET} active! ~~~\n"
    )


@client.event
async def on_message(message):
    # Anti-Rickroll.
    await client.process_commands(message)
    channel = client.get_channel(message.channel.id)

    if message.content == "https://youtu.be/dQw4w9WgXcQ":
        await message.delete()
        await channel.send(f"{message.author.mention}: Nope! No rick-rolling while I'm in town!")


@client.command(aliases=["poke"])
async def pokemon(ctx):

    def check(m):
        return m.author == ctx.author

    found = False
    request = requests.get("https://pokeapi.co/api/v2/pokemon/")
    request_json = request.json()["results"]

    await ctx.send(f"{ctx.author.mention}: Enter the name of your pokemon!")
    required = await client.wait_for("message", check=check)

    for dictionary in request_json:
        if dictionary["name"] == required.content.lower():
            info_url, found = dictionary["url"], True
            break

    if found == True:
        info_request = requests.get(info_url)
        info_request_json_pngs = info_request.json()["sprites"]
        info_request_json_stats = info_request.json()["stats"]

        base_stat_array = []

        for dictionary in info_request_json_stats:
            base_stat_array.append(dictionary["base_stat"])

        embeded_message = discord.Embed(
            title=f"Pokemon: {required.content.lower()}", description=f"This will give you all of the information regarding {required.content.lower()}!", colour=discord.Colour.dark_gray())

        embeded_message.set_thumbnail(
            url=info_request_json_pngs["front_default"])

        embeded_message.add_field(
            name="Base health:", value=f"The pokemon {required.content.lower()} has a base health of {base_stat_array[0]}.")

        embeded_message.add_field(
            name="Base attack:", value=f"The pokemon {required.content.lower()} has a base attack of {base_stat_array[1]}."
        )

        embeded_message.add_field(
            name="Base defense:", value=f"The pokemon {required.content.lower()} has a base defense of {base_stat_array[2]}."
        )

        embeded_message.add_field(
            name="Base special attack:", value=f"The pokemon {required.content.lower()} has a base special attack of {base_stat_array[3]}."
        )

        embeded_message.add_field(
            name="Base special defense:", value=f"The pokemon {required.content.lower()} has a base special defense of {base_stat_array[4]}."
        )

        embeded_message.add_field(
            name="Base speed:", value=f"The pokemon {required.content.lower()} has a base speed of {base_stat_array[5]}."
        )

        await ctx.send(ctx.author.mention, embed=embeded_message)

    else:
        await ctx.send(f"{ctx.author.mention}: Sorry, I couldn't find that pokemon..")


@client.command(aliases=["calc"])
async def calculator(ctx):

    def check(m):
        return m.author == ctx.author

    await ctx.send(f"{ctx.author.mention}: Enter your first number!")
    number_1 = await client.wait_for("message", check=check)

    try:
        number_1 = int(number_1.content)

    except:
        await ctx.send(f"{ctx.author.mention}: That's not a number yo..")
        return

    await ctx.send(f"{ctx.author.mention}: Enter your operator!")
    operator = await client.wait_for("message", check=check)

    if operator.content not in ("*", "/", "+", "-"):
        await ctx.send(f"{ctx.author.mention}: That's not an operator yo..")
        return

    await ctx.send(f"{ctx.author.mention}: Enter your second number!")
    number_2 = await client.wait_for("message", check=check)

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


@client.command(aliases=["hi"])
# This decorator will intake a function to be used as a discord command.
# The parameter aliases intakes a list of strings to be used as ways of calling the command function.
async def hello(ctx):
    # The ctx perameter referes to the context of the conversation between
    # the person calling the bot and the bot itself and is always required in a command function.
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
    # When the astrix symbol is passed through a command that recieves a question it tells discord include all following words as the question.
    # I'm not too sure what discord does with the astrix, but I do know it's used to instantiate a key
    # arguments parameter and unpack lists in other cases.

    def check(m):
        return m.author == ctx.author

    await ctx.send(f"{ctx.author.mention}: Hey, ask me a yes or no question!")
    question = await client.wait_for("message", check=check)

    with open("Python/BOT/responses.txt") as random_responses_file:
        random_responses_list = []

        for element in random_responses_file.readlines():
            if element.__contains__("\n"):
                random_responses_list.append(element[:-1])

            else:
                random_responses_list.append(element)

        random_response = random.choice(random_responses_list)

    await ctx.send(f"{ctx.author.mention}: \"{question.content}\" -- {random_response}")

with open("Python/BOT/token.txt") as file:
    os.system("clear")
    # This reads the file containing the discord bot's token.

    client.run(file.read())
