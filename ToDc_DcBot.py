# Sends messages into the dc

import json
import os

import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
signal_running = True
telegram_running = True

with open("config_own.json", "r") as read_file:
    data = json.load(read_file)
sendChannelID = data["discord"]["SignalDiscordChatId"]


@bot.command()
async def myloop_signal(ctx):
    old_text = ""
    while signal_running:
        print("Loop running")
        with open("messageCarrierFromSignal.txt") as file:
            text = file.read()
            print(f"current text = {text}")
        new_text = text
        if new_text != old_text:
            print(f"sending: {text}")
            await send_message(sendChannelID, text)
            old_text = new_text
        await asyncio.sleep(1)


@bot.command()
async def myloop_telegram(ctx):
    old_text = ""
    while telegram_running:
        print("Loop running")
        with open("messageCarrierFromTelegram.txt") as file:
            text = file.read()
            print(f"current text = {text}")
        new_text = text
        if new_text != old_text:
            print(f"sending: {text}")
            await send_message(sendChannelID, text)
            old_text = new_text
        await asyncio.sleep(1)


async def send_message(channel_id, message):
    await bot.get_channel(channel_id).send(message)


@bot.event
async def on_ready():
    print('Bot is ready.')
    # await myloop_signal()
    # await myloop_telegram()


def run_bot():
    bot.run(data["discord"]["SignalToDc_BotToken"])


if __name__ == '__main__':
    run_bot()