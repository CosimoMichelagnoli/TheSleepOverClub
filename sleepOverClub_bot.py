	#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot

f = open("token.txt", r)
API_TOKEN = f.read()

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
I'm back!! Forse sono un pò più utile... ma posso ancora migliorare.\
Per visionare i pochi comandi implementati usa il comando /help.
""")
@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, """\
Lo so, non so ancora fare un cazzo...\n
Un po' perchè mancano le idee, un po' perchè quelle che ci sono sono complesse fino a che il coglione che mi sta programmando non impara a usare le API.\n 
Lamentele a parte...\n
Con il comando /serieA oppure /serieC, vi dirò come il rugby ha deciso i vostri programmi della settimana. Quindi oltre a ricordarvi della tassa del rugby per ora sono inutile.\n Grazie per l'attenzione. (Samoa, ogni tanto batti un colpo <3)
""")
@bot.message_handler(commands=['serieA'])
def send_welcome(message):
    bot.reply_to(message, """\
Lunedì: 17:00 - 20:00(palestra individuale)\n
Martedì: 19:00 - 21:00(campo + palestra)\n
Mercoledì: 19:00 - 21:00(campo)\n
Giovedì: 17:00 - 20:00(palestra indivisuale)\n
Venerdì: 19:30 - 21:00(campo)\

""")
@bot.message_handler(commands=['serieC'])
def send_welcome(message):
    bot.reply_to(message, """\
Lunedì: riposo\n
Martedì: 20:00 - 21:30(campo + palestra)\n
Mercoledì: 17:00 - 20:00(palestra indivisuale)\n
Giovedì: 20:00 - 21:30(campo + palestra)\n
Venerdì: 17:00 - 20:00(palestra indivisuale) 20:00 - 21:30(campo)\n

""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#@bot.message_handler(func=lambda message: True)
#def echo_message(message):	
    #bot.reply_to(message, message.text)


bot.polling()





