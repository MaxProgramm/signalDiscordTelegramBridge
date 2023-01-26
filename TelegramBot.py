import json
import os
import time
from datetime import datetime

import telebot

with open("config_own.json", "r") as read_file:
    data = json.load(read_file)
sendChannelID = data["discord"]["SignalDiscordChatId"]

BOT_TOKEN = data["telegram"]["bot_token"]

bot = telebot.TeleBot(BOT_TOKEN, num_threads=3)
dc_running = False
signal_running = False

#@bot.message_handler(commands=["hello", "hi"])
#@bot.message_handler()
#def send_welcome(message: telebot.types.Message):
#    bot.reply_to(message, "Hi, I' am a bot!")


def send_msg_to_signal(msg):
    print("should send to signal")
    curl_command = f"""curl -X POST -H "Content-Type: application/normal" -d '{"{"}"message": "{msg}", "number": "{data["signal"]["phone_number"]}", "recipients": [{'"'}{data["signal"]["group_id"]}{'"'}]{"}"}' '{data["signal"]["signal_service"]}/v2/send'"""
    os.system(curl_command)


def write_into_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)


# Sends the Discord messages into chat
@bot.message_handler(commands=["discord_loop_start"])
def loop_messages_to_tele_discord(message: telebot.types.Message):
    global dc_running
    if dc_running == False:
        old_text = ""
        dc_running = True
        while dc_running:
            bot.set_state(bot.user.id, "On", message.chat.id)
            print("lopping")
            with open("messageCarrierFromDc.txt") as file:
                print("opening file: messageCarrierFromDc.txt")
                text = file.read()

            new_text = text
            if new_text != old_text:
                print(f"sending msg: {new_text}")
                bot.send_message(message.chat.id, new_text)
                old_text = new_text
            time.sleep(1)
    else:
        bot.send_message(message.chat.id, "Already forwarding Discord messages")


# Stops the sending of discord messages into chat
@bot.message_handler(commands=["discord_loop_stop"])
def stop_loop_messages_discord(message: telebot.types.Message):
    global dc_running
    print("Received discord stop command")
    if dc_running:
        print("Forwarding discord messages stopped")
        dc_running = False
        bot.set_state(bot.user.id, "Off", message.chat.id)
        bot.send_message(message.chat.id, "Forwarding Discord messages stopped")
    else:
        bot.send_message(message.chat.id, "Forwarding discord messages already stopped")


# Starts the sending of signal messages
@bot.message_handler(commands=["signal_loop_start"])
def loop_messages_to_tele_signal(message: telebot.types.Message):
    global signal_running
    if signal_running == False:
        old_text = ""
        signal_running = True
        while signal_running:
            bot.set_state(bot.user.id, "On", message.chat.id)
            print("lopping")
            with open("messageCarrierFromSignal.txt") as file:
                print("opening file: messageCarrierFromSignal.txt")
                text = file.read()

            new_text = text
            if new_text != old_text:
                print(f"sending msg: {new_text}")
                bot.send_message(message.chat.id, new_text)
                old_text = new_text
            time.sleep(1)
    else:
        bot.send_message(message.chat.id, "Already forwarding Discord messages")


# Stops the sending of signal messages into chat
@bot.message_handler(commands=["signal_loop_stop"])
def stop_loop_messages_signal(message: telebot.types.Message):
    global signal_running
    print("Received signal stop command")
    if signal_running:
        print("Forwarding signal messages stopped")
        signal = False
        bot.set_state(bot.user.id, "Off", message.chat.id)
        bot.send_message(message.chat.id, "Forwarding signal messages stopped")
    else:
        bot.send_message(message.chat.id, "Forwarding signal messages already stopped")


@bot.message_handler(func=lambda msg: True)
def forward_messages_to_discord_and_signal(message: telebot.types.Message):
    print("received message")
    timestamp = message.date
    dt_object = datetime.fromtimestamp(timestamp)
    time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    if signal_running:
        print("sending to signal")
        send_msg_to_signal(f"{time} | {message.from_user.full_name} | {message.text}")
    if dc_running:
        print("Writing to dc")
        write_into_file("messageCarrierFromTelegram.txt", f"{time} | {message.from_user.full_name} | {message.text}")


bot.infinity_polling()

print("Finish!")