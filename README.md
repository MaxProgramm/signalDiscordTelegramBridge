# signalDiscordTelegramBridge
This is  a ppject, which allows You to connect a discord signal, discord and telegram group. When a message is send in one of them, it automatically gets forwarded to the other groups.

For signal, it uses the signal-cli-rest-api, by bbernhard, (see https://github.com/bbernhard/signal-cli-rest-api), which creates a small dockerized REST API around signal-cli.
Signal-cli is made by AsamK, (see https://github.com/AsamK/signal-cli)
Huge thanks to these guys.

For Discord i use the official discord.py, by Discord.

For Telegram i use the pyTelegramBotAPI, ( see https://pypi.org/project/pyTelegramBotAPI/), which is a simple, but extensible Python implementation for the Telegram Bot API.

You can configure everything in the config.json.

For handling incoming and outgoing messages on the discord server i am using two seperate discord bots. Ones job is to receive discord messages from the other services/bots and send them into the discord chat, the others job is to receive discord messages in the discord chat and forward them to the other bots / services. The translation betwenn the different bots, is made possible through text files and Http reqests.


