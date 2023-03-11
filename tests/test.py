from unittest import IsolatedAsyncioTestCase

from tests.stub_classes import Message, User, Channel
from tests.test_bot import TestBot


class TestCommands(IsolatedAsyncioTestCase):

    async def get_test_data(self):
        hello_bot = TestBot()
        hello_bot.run("no-token")

        await hello_bot.on_ready()

        msg = Message()
        msg.author = User()
        msg.channel = Channel()
        return msg, hello_bot

    async def test_false_command(self):
        msg, hello_bot = await self.get_test_data()

        msg.content = "/notfound"
        await hello_bot.on_message(msg)

        self.assertTrue("" == msg.channel.last_message)

    async def test_normal_message(self):
        msg, hello_bot = await self.get_test_data()

        msg.content = "normal message"
        await hello_bot.on_message(msg)

        self.assertTrue("" == msg.channel.last_message)

    async def test_command(self):
        msg, hello_bot = await self.get_test_data()

        msg.content = "help"
        await hello_bot.on_message(msg)

        self.assertTrue(msg.channel.last_message.startswith("Available commands:"))
        self.assertTrue("```yaml" in msg.channel.last_message)
        self.assertTrue("This bot has no commands." in msg.channel.last_message)
        self.assertTrue(msg.channel.last_message.endswith("```"))

        # result = await
