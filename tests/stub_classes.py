class Channel:
    last_message: str = ""

    async def send(self, content: str):
        self.last_message = f"{content}"
        print("sent:\n", self.last_message)


class Message:
    author = None
    content: str = "test:content"
    channel: Channel


class User:
    name: str = "test:name"
    nick: str = "test:nick"
