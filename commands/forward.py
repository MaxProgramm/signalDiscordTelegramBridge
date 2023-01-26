from datetime import datetime
from signalbot import Command, Context
import signalbot


class ForwardCommand(Command):
    def describe(self) -> str:
        return "🏓 Forward: Forwards message to discord"

    async def handle(self, c: Context):
        msg = c.message.text
        author = c.message.source
        timestamp = c.message.timestamp
        dt_object = datetime.fromtimestamp(timestamp / 1000)
        time = dt_object.strftime('%Y-%m-%d %H:%M:%S')

        print(f"Received Message: {time} | {author}: {msg}")
        with open("messageCarrierFromSignal.txt", "w") as file:
            file.write(f"{time} | {author}: {msg}")

        return
