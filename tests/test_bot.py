import logging
from dataclasses import MISSING
from typing import Any, Optional

import discord
from discord import Message, Intents

from mehlbot import command_callback
from mehlbot.command import bot_commands
from mehlbot.logger import setup_logger

logger = setup_logger(__name__)


class TestBot(discord.Client):
    """
    Slightly different version from hello_bot.py
    """

    def __init__(self, *, intents: Intents = discord.Intents.all(), **options: Any) -> None:
        super().__init__(intents=intents, **options)

    def run(
            self,
            token: str,
            *,
            reconnect: bool = True,
            log_handler: Optional[logging.Handler] = MISSING,
            log_formatter: logging.Formatter = MISSING,
            log_level: int = MISSING,
            root_logger: bool = False,
    ) -> None:
        pass

    async def on_ready(self) -> None:
        logger.info("Bot started.")

    async def on_message(self, message: Message):
        # ignore messages from the bot itself
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
