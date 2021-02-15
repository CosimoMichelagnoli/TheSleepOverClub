"""
Simple Bot to reply to Telegram messages taken from the python-telegram-bot examples.
Deployed using heroku.
Author: liuhh02 https://medium.com/@liuhh02
"""

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from datetime import time
import os
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = 'YourToken'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    update.message.reply_text("""\
I'm back!! Forse sono un pò più utile... ma posso ancora migliorare.\n
Per visionare i pochi comandi implementati usa il comando /help.
""")

def seriea(update, context):
    """Send a message when the command /serieA is issued."""
    update.message.reply_text("""\
Lunedì: 17:00 - 20:00(palestra individuale)\n
Martedì: 19:00 - 21:00(campo + palestra)\n
Mercoledì: 19:00 - 21:00(campo)\n
Giovedì: 17:00 - 20:00(palestra individuale)\n
Venerdì: 19:30 - 21:00(campo)\

""")

def seriec(update, context):
    update.message.reply_text("""\
Lunedì: riposo\n
Martedì: 20:00 - 21:30(campo + palestra)\n
Mercoledì: 17:00 - 20:00(palestra individuale)\n
Giovedì: 20:00 - 21:30(campo + palestra)\n
Venerdì: 17:00 - 20:00(palestra individuale) 20:00 - 21:30(campo)\n

""")

def contaIppo(update, context):
    countIppo = 0

def addCount(update, context, hash_table):
    if update.message.text.lower() != 'ippo':
	return
    if search(hash_table, update.message.from.id) != None:
        return
   countIppo += 1
   insert(hash_table, update.message.from.id, update.message.from.first_name)
  

    
def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("""\
Lo so, non so ancora fare un cazzo...\n
Un po' perchè mancano le idee, un po' perchè quelle che ci sono sono complesse fino a che il coglione che mi sta programmando non impara a usare le API.\n 
Lamentele a parte...\n
Con il comando /seriea oppure /seriec, vi dirò come il rugby ha deciso i vostri programmi della settimana. Quindi oltre a ricordarvi della tassa del rugby per ora sono inutile.\n Grazie per l'attenzione.
""")

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def buongiornoDido(context: CallbackContext):
    context.bot.send_message(chat_id=UserId, 
                             text='Buongiorno,potrei essere in ritardo, luzi 9.15...')

def insert(item_list, key, value):
    item_list.append((key, value))
 
def search(item_list, key):
    for item in item_list:
        if item[0] == key:
            return item[1]
#def countAndVote(update, context):
 #   if !search(update.message.from.first_name):
#	add(update.message.from.first_name)
 #   increment(update.message.from.first_name)
  #  if update.message.text == 'up':
#	checkIfPossibleUp(update.message.from.first_name)
 #   elif update.message.text == 'ban':
#	checkIfPossibleBan(update.message.from.first_name)
    
def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    hash_table = [[] for _ in range(12)]
    updater = Updater(TOKEN, use_context=True)


    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    job = updater.job_queue
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("seriea", seriea))
    dp.add_handler(CommandHandler("seriec", seriec))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("contaippo", contaIppo(hash_table)))
    dp.add_handler(MessageHandler(Filters.text, addCount))
    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, countAndVote))
    job.run_once(buongiornoDido, time(11,3,0))
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://pacific-gorge-77157.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
