#adding imports
import telebot
import os
import hashlib
import base64
import string

#bot token
token = "INSERT BOT TOKEN HERE"

arr= [""]

#initializing telebot lib
bot = telebot.TeleBot(token)

#starting greet
@bot.message_handler(commands=["start"])
def Greet(message):
    bot.send_message(message.chat.id, "/list to list all commands")

#list all commands
@bot.message_handler(commands=["list"])
def List(message):
    bot.send_message(message.chat.id, "/base64 for base64 encoding\n /base64decode for base64 decoding\n /md5 for md5 hashing")

#base64 encode
@bot.message_handler(commands=["base64"])
def Enc64(message):
    text = message.text.replace("/base64", "")
    text.strip()
    for item in arr:
        if item == text:
            bot.send_message(message.chat.id, "Please, send /base64 *your text*")
        else:
            text = os.linesep.join([s for s in text.splitlines() if s])
            enc = base64.b64encode(text.encode('ascii'))
            bot.reply_to(message, enc)

#base64 decode
@bot.message_handler(commands=["base64decode"])
def Enc64dec(message):
    text = message.text.replace("/base64decode", "")
    text.strip()
    text = os.linesep.join([s for s in text.splitlines() if s])
    dec = base64.b64decode(text.encode('ascii'))
    bot.reply_to(message, dec)

#md5 hashing
@bot.message_handler(commands=["md5"])
def EncMd5(message):
    text = message.text.replace("/md5","")
    text.strip()
    text = os.linesep.join([s for s in text.splitlines() if s])
    text = hashlib.md5(text.encode()).hexdigest()
    bot.reply_to(message, text)



bot.polling()


