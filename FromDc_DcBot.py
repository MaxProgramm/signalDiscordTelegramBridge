# Exports messages from the dc

import json
import os

import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
dc_running = True

with open("config_own.json", "r") as read_file:
    data = json.load(read_file)
sendChannelID = data["discord"]["SignalDiscordChatId"]


def send_msg_to_signal(msg):
    print("should send to signal")
    curl_command = f"""curl -X POST -H "Content-Type: application/normal" -d '{"{"}"message": "{msg}", "number": "{data["signal"]["phone_number"]}", "recipients": [{'"'}{data["signal"]["group_id"]}{'"'}]{"}"}' '{data["signal"]["signal_service"]}/v2/send'"""

    os.system(curl_command)



@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_message(message: discord.Message):
    if message.author.id != bot.user.id and message.author.id != data["discord"]["SignalToDc_BotId"] and message.channel.id == sendChannelID:
        if message.content != "!myloop_signal" and message.content != "!myloop_telegram":
            print("received message not from bot")
            time = message.created_at.strftime('%Y-%m-%d %H:%M:%S')
            msg = f"{time} | {message.author} | {message.content}"
            send_msg_to_signal(msg)
            print("should write into file")
            with open("messageCarrierFromDc.txt", "w") as file:
                file.write(msg)


def run_bot():
    bot.run(data["discord"]["DcToSignal_BotToken"])


if __name__ == '__main__':
    run_bot()