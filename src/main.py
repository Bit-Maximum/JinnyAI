import os
from dotenv import load_dotenv

from JinnyAIBot import JannyAIBot

import discord

default_params = {
    # including this with your server id in place of mine will localize slash functions to your server
    # (won't appear for other servers bot is in)
    "guild_ids": ["1340696522831953935"]
}


if __name__ == "__main__":
    load_dotenv()

    bot = JannyAIBot()
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))
