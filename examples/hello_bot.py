"""" Template" bot for copy-paste usage."""
from pathlib import Path

import discord
from discord import Intents, Member, Message

from mehlbot import command_callback
from mehlbot.command import bot_commands
from mehlbot.logger import setup_logger


logger = setup_logger(__name__)


class HelloBot(discord.Client):
    """Hello bot (as in hello world bot) that has no additional commands than
    the default 'help' command (see commands.py)."""

    def __init__(self, intents: Intents, **options) -> None:
        super().__init__(intents=intents, **options)

    async def on_ready(self) -> None:
        """Gets called when bot is ready/started."""
        logger.info("Bot started.")

    async def on_message(self, message: Message):
        """Called whenever the discord bot sees a message.

        :param message: received message
        """
        # ignore messages from the bot itself
        assert isinstance(message.author, Member)
        if message.author == self.user:
            return

        # check if the message is a command
        command_found = await command_callback.process_command(self, bot_commands, message)

        # log message and prepend command
        log_msg = ""
        if command_found:
            log_msg += "command: "

        log_msg += f"{message.author.nick} ({message.author.name}): '{message.content}'"
        logger.info(log_msg)


def main():
    """Create bot and load the discord api from file.

    (in .gitignore).
    """
    hello_bot = HelloBot()

    with Path("token.txt").open() as file:
        token = file.read()
    hello_bot.run(token)
