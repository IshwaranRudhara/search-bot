from telegram.ext import CommandHandler, run_async
from bot import dispatcher, updater, botStartTime
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import *
from .helper.telegram_helper.filters import CustomFilters
from .modules import authorize, list


@run_async
def log(update, context):
    sendLogFile(context.bot, update)

def main():

    log_handler = CommandHandler(BotCommands.LogCommand, log, filters=CustomFilters.owner_filter)

    dispatcher.add_handler(log_handler)

    updater.start_polling()
    updater.idle()
    LOGGER.info("Yeah I am running!")

main()
