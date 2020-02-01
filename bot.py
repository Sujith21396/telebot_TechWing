
# Imports
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

# Variables
updater = Updater(token='952779034:AAETrfh1DVqsA3rJf0QddKos2XOy3IwrfDM', use_context=True)
dispatcher = updater.dispatcher

# Functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bigileyyyyyyyy")
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
def setDate(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Temp")
def setHoroscope(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="WuhanVirus")    

# Main
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

date_handler = CommandHandler('setDate', setDate)
dispatcher.add_handler(date_handler)

horoscope_handler = CommandHandler('setHoroscope', setHoroscope)
dispatcher.add_handler(horoscope_handler)


updater.start_polling()
print("Bot is Working")
