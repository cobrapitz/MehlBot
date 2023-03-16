"""Contains the actual tests for the Discord bot."""
import unittest
from unittest import IsolatedAsyncioTestCase

import discord

from tests.bot import TestBot
from tests.stub_classes import Channel, Message, User


class TestCommands(IsolatedAsyncioTestCase):
    """Test class that contains all tests."""

    async def get_test_data(self) -> tuple[Message, TestBot]:
        """Get minimal data (bot and message) to test the bot."""
        hello_bot = TestBot(discord.Intents.all())
        hello_bot.run("no-token")

        await hello_bot.on_ready()

        msg = Message()
        msg.author = User()
        msg.channel = Channel()
        return msg, hello_bot

    async def test_false_command(self):
        """Check if a not valid command is a command."""
        msg, hello_bot = await self.get_test_data()

        msg.content = "hel"
        await hello_bot.on_message(msg)  # type: ignore

        assert msg.channel.last_message == ""

    async def test_normal_message(self):
        """Check if a regular message counts as a."""
        msg, hello_bot = await self.get_test_data()

        msg.content = "Does the bot have a help command?"
        await hello_bot.on_message(msg)  # type: ignore

        assert msg.channel.last_message == ""

    async def test_command(self):
        """Check if the help command prints the expected output."""
        msg, hello_bot = await self.get_test_data()

        msg.content = "help"
        await hello_bot.on_message(msg)  # type: ignore

        assert msg.channel.last_message.startswith("Available commands:")
        assert "```yaml" in msg.channel.last_message
        assert "This bot has no commands." in msg.channel.last_message
        assert msg.channel.last_message.endswith("```")


if __name__ == "__main__":
    unittest.main()
