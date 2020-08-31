diceArr = ["Vacuum floor","Cook","Wash dishes","Rest","Go to supermarket","Take out garbage"]
import random
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm THE GOD OF BOTS...")
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! yOu SaID " + update.message.text)
def dice(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(diceArr))

updater = Updater(token='1187785181:AAGLGNddzyqx4wY8bSRhByMAZtWlQZPBKhY', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dice_handler = CommandHandler('houseworkdice', dice)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(dice_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


updater.start_polling()
