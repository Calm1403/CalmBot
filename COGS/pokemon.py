from discord.ext import commands
from colorama import Fore as F
import requests
import discord


class pokemon(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"~~~ The pokemon.py cog has been {F.GREEN}loaded{F.RESET}! ~~~")

    @commands.command(aliases=["poke"])
    async def pokemon(self, ctx):
        # This function will use the pokemon API to display information regarding a certain pokemon.

        def check(m):
            # This function checks to see if the author of the 'wait_for' message is equal
            # to the author of the context.
            return m.author == ctx.author

        await ctx.send(f"{ctx.author.mention}: Enter the name of your pokemon! :smile:")
        required = await self.client.wait_for("message", check=check)
        await ctx.send(f"{ctx.author.mention}: Aight, give me a sec to look for {required.content.lower()}..")

        found = False
        request_1 = requests.get(
            "https://pokeapi.co/api/v2/pokemon/")

        request_2 = requests.get(
            "https://pokeapi.co/api/v2/pokemon/?offset=20&limit=20")

        request_3 = requests.get(
            "https://pokeapi.co/api/v2/pokemon/?offset=40&limit=20")

        request_4 = requests.get(
            "https://pokeapi.co/api/v2/pokemon/?offset=60&limit=20"
        )

        request_5 = requests.get(
            "https://pokeapi.co/api/v2/pokemon/?offset=80&limit=20")

        request_6 = requests.get(
            "https://pokeapi.co/api/v2/pokemon/?offset=100&limit=20"
        )

        # These are the requests to the poke api; each being a list of dictionaries with elements containing various pokemon.

        requests_in_json = [
            request_1.json()["results"],
            request_2.json()["results"],
            request_3.json()["results"],
            request_4.json()["results"],
            request_5.json()["results"],
            request_6.json()["results"]
        ]

        # This gets the response json data and focuses on the API-key named results.

        for request in requests_in_json:
            if found == True:
                # If found is equal to true break from loop to prevent searching through a different request
                # even after the required pokemon has been found.
                break

            for dictionary in request:
                # For each dictionary in the result_json list.
                if dictionary["name"] == required.content.lower():
                    # If dictionary element of title 'name' is equal to the 'wait_for' message content in lower case.
                    info_url, found = dictionary["url"], True
                    # Variable info_url is equal to the found dictionary element 'url' and variable found is equal to True
                    break
                    # Break from nested loop to prevent itterating further after finding required pokemon.

        # NOTE to all my fellow programmer friends:

        # Forgive me if this method of searching
        # for pokemon is cringe, results
        # in poor times, and is considered a warcrime against humanity.
        # It was the only way I could think of searching for elements in a dictionary within a
        # dictionary within a list haha..
        # It's a temporary solution until I figure out a better strategy. :)

        if found == True:
            # If variable found is equal to True.
            info_request = requests.get(info_url)
            # This makes a request to the found url.
            info_request_json_pngs = info_request.json()["sprites"]
            # This gets the pokemon sprite json data.
            info_request_json_stats = info_request.json()["stats"]
            # This gets the pokemon stat json data.

            base_stat_array = []

            # This array is used to access each base stat.
            # Position one refers to base health.
            # Position two refers to base attack.
            # Position three refers to base defence.
            # Position four refers to base special attack.
            # Position five refers to base special attack.
            # Position six refers to base speed.

            for dictionary in info_request_json_stats:
                # For each dictionary in the json_stats.
                base_stat_array.append(dictionary["base_stat"])
                # Append dictionary base state element.

            embeded_message = discord.Embed(
                # This creates an embeded message.
                title=f"Pokemon: {required.content.lower()}", description=f"This will give you all of the information regarding {required.content.lower()}!", colour=discord.Colour.dark_gray()
            )

            embeded_message.set_thumbnail(
                # This sets the embeded message's thumbnail.
                url=info_request_json_pngs["front_default"]
            )

            embeded_message.add_field(
                # This adds a field to be added to the embeded message.
                name="Base health:", value=f"The pokemon {required.content.lower()} has a base health of {base_stat_array[0]}."
            )

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
            # This sends the embeded message.

        else:
            # If the variable found is not equal to true:
            await ctx.send(f"{ctx.author.mention}: Sorry, I couldn't find that pokemon..")


async def setup(client):
    # When "loading" a cog, discord will check to see if there is a setup function to be used as a gateway into the cog.
    await client.add_cog(pokemon(client))
    # Discord then adds the cog to be used using an instance of the cog class.
