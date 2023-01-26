# signalDiscordTelegramBridge
This is  a ppject, which allows You to connect a discord signal, discord and telegram group. When a message is send in one of them, it automatically gets forwarded to the other groups.

For signal, it uses the signal-cli-rest-api, by bbernhard, (see https://github.com/bbernhard/signal-cli-rest-api), which creates a small dockerized REST API around signal-cli.
Signal-cli is made by AsamK, (see https://github.com/AsamK/signal-cli)
Huge thanks to these guys.

For Discord i use the official discord.py, by Discord.

For Telegram i use the pyTelegramBotAPI, ( see https://pypi.org/project/pyTelegramBotAPI/), which is a simple, but extensible Python implementation for the Telegram Bot API.
