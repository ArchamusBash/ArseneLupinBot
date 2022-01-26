#adding imports
import telegram
import telebot
import os
import hashlib
import base64

#bot token and other data
#token = os.getenv("API_KEY")
token = '5064313232:AAFMGpe3zyFpcIxgFcU6UBmwAY3YvQaM0g0'
#admin = os.getenv("admin")
admin = 1808619177
#channel = os.getenv("channel")
channel = -1001537285475

#empty array for comparisons
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
    bot.send_message(message.chat.id, "/base64 for base64 encoding\n /base64decode for base64 decoding\n /md5 for md5 hashing\n /feedback to send feedback to admin")

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
    for item in arr:
        if item == text:
            bot.send_message(message.chat.id, "Please, send /base64decode *your text*")
        else:
            text = os.linesep.join([s for s in text.splitlines() if s])
            dec = base64.b64decode(text.encode('ascii'))
            bot.reply_to(message, dec)

#md5 hashing
@bot.message_handler(commands=["md5"])
def EncMd5(message):
    text = message.text.replace("/md5","")
    text.strip()
    for item in arr:
        if item == text:
            bot.send_message(message.chat.id, "Please, send /md5 *yout text*")
        else:
            text = os.linesep.join([s for s in text.splitlines() if s])
            text = hashlib.md5(text.encode()).hexdigest()
            bot.reply_to(message, text)

#feedback command
@bot.message_handler(commands=["feedback"])
def Feedback(message):
    feedback = bot.send_message(message.chat.id, "Write your feedback, feel free to suggest anything.")
    bot.register_next_step_handler(feedback, Send)

#new feedback method
def Send(message):
    bot.send_message(message.chat.id, "Thank you for your feedback!")
    bot.forward_message(channel, message.chat.id, message.id)

#old feedback method
def OldSend(message):
    name = str(message.text)
    doc = open("feedback.txt", "w", encoding="utf-8").write(name)
    bot.send_document(admin, doc)

bot.polling()
