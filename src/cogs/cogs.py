"""
Loads a predefined list of cogs into the bot.

This function iterates over a list of cog names and loads each
cog as an extension into the provided bot instance.

Parameters:
    bot: The bot instance to which the cogs will be loaded.
"""


def cogs_setup(bot):
    cogs_list = [
        "voice",
    ]

    for cog in cogs_list:
        bot.load_extension(f"cogs.{cog}")
