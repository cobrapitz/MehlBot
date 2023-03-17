"""Mock/Stub for the Discord bot class."""
import logging
from dataclasses import MISSING
from typing import Optional

import discord
from discord import Intents, Message

from mehlbot import command_callback
from mehlbot.command import bot_commands
from mehlbot.logger import setup_logger
from tests.stub_classes import Member


logger = setup_logger(__name__)


class TestBot(discord.Client):
    """Slightly different version from hello_bot.py.

    Stub run method.
    """

    def __init__(self, intents: Intents, **options) -> None:
        super().__init__(intents=intents, **options)

    def run(
        self,
        token: str,
        *,
        reconnect: bool = True,
        log_handler: Optional[logging.Handler] = MISSING,  # type: ignore
        log_formatter: logging.Formatter = MISSING,  # type: ignore
        log_level: int = MISSING,  # type: ignore
        root_logger: bool = False,
    ) -> None:
        """Overridden run method, that doesn't require a valid Discord
        token."""

    async def on_ready(self) -> None:
        """Ready method, called when bot is started."""
        logger.info("Bot started.")

    async def on_message(self, message: Message):
        """Whenver message is received from Discord."""
        assert isinstance(message.author, Member)
        if message.author == self.user:
            return

        command_found = await command_callback.process_command(self, bot_commands, message)

        log_msg = ""
        if command_found:
            log_msg += "command: "

        log_msg += f"{message.author.nick} ({message.author.name}): '{message.content}'"
        logger.info(log_msg)
