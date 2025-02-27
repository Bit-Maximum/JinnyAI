import discord

from utils.service.llm_worker import LLMWorker
from utils.service.openapi_driver import OpenAIDriver
from utils.logging_worker.logging_worker import setting_up_logging

from cogs.cogs import cogs_setup


class JannyAIBot(discord.Bot):
    """
    A Discord bot class that integrates with an LLM service to respond to messages.

    Attributes:
        llm_worker (LLMWorker): An instance of LLMWorker initialized with OpenAIDriver.

    Events:
        on_ready(): Prints a message when the bot is ready.
        on_message(message): Processes messages, retrieves a response from the LLM, and sends it back to the channel.
    """

    def __init__(self):
        setting_up_logging()
        super().__init__(intents=discord.Intents.all())
        self.llm_worker = LLMWorker(OpenAIDriver())
        cogs_setup(self)

    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.author.id == self.application_id:
            return

        print(f"{message.author} said: {message.content}")
        query = self.llm_worker.rug_message(message)
        resource = self.llm_worker.get_response(query)
        print(f"Answer: {resource}")
        await message.channel.send(resource)
