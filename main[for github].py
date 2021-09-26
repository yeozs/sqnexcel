import os
import telebot
from flask import Flask, request

TOKEN = '<type your telebot token here>'
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing? \n Answer with the following replies \n /parade_state \n /sarprogramme \n /126parade_state \n /flyingprogramme \n Thank you")

@bot.message_handler(commands=['hello'])
def send_welcome(message):
	bot.send_message(message.chat.id, "hello")

@bot.message_handler(commands=['parade_state'])
def get_ps(message):
  with open("sqnexcel.csv","rb") as misc:
    f=misc.read()
  bot.send_message(message.chat.id,f)



@bot.message_handler(commands=['sarprogramme'])
def get_sar(message):
  with open("sarprogramme.csv","rb") as misc1:
    g=misc1.read()
  bot.send_message(message.chat.id,g)


@bot.message_handler(commands=['126parade_state'])
def get_ps(message):
  with open("126sqnexcel.csv","rb") as misc2:
    h=misc2.read()
  bot.send_message(message.chat.id,h)

@bot.message_handler(commands=['flyingprogramme'])
def get_ps(message):
  with open("flyingprogramme.csv","rb") as misc3:
    j=misc3.read()
  bot.send_message(message.chat.id,j)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
   bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
   return "!", 200

@server.route("/")
def webhook():
   bot.remove_webhook()
   bot.set_webhook(url='<type your Heroku web URL here>' + TOKEN)
   return "!", 200

if __name__ == "__main__":
   server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
