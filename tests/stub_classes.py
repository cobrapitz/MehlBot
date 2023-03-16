"""Stub classes to test without valid token."""


class Channel:
    """Discord channel class with only the tested methods."""

    last_message: str = ""

    async def send(self, content: str):
        """Doesn't actually send, instead add store the message for testing."""
        self.last_message = f"{content}"


class User:
    """User class  with necessary test data."""

    name: str = "test:name"
    nick: str = "test:nick"


class Message:
    """Message class with necessary test data."""

    author: User
    content: str = "test:content"
    channel: Channel
