import os
from signalbot import SignalBot
from commands import PingCommand, FridayCommand, TypingCommand, TriggeredCommand, ForwardCommand
from signalbot import Command, Context
import logging
import json

with open("config_own.json", "r") as read_file:
    data = json.load(read_file)


logging.getLogger().setLevel(logging.INFO)
logging.getLogger("apscheduler").setLevel(logging.WARNING)


def main():
    print(data["signal"]["phone_number"])
    signal_service = data["signal"]["signal_service"]
    phone_number = data["signal"]["phone_number"]
    group_id = data["signal"]["group_id"]
    internal_id = data["signal"]["internal_id"]

    config = {
        "signal_service": signal_service,
        "phone_number": phone_number,
        "storage": None,
    }
    bot = SignalBot(config)

    bot.listen(group_id, internal_id)

    bot.register(PingCommand())
    bot.register(FridayCommand())
    bot.register(TypingCommand())
    bot.register(TriggeredCommand())
    bot.register(ForwardCommand())

    bot.start()

    print("has started")

if __name__ == "__main__":
    main()

