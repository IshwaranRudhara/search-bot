from telegram.ext import CommandHandler, run_async
from bot.helper.drive_utils.gdriveTools import GoogleDriveHelper
from bot import LOGGER, dispatcher
from bot.helper.telegram_helper.message_utils import sendMessage, editMessage
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.bot_commands import BotCommands

@run_async
def list_drive(update,context):
    try:
        search = update.message.text.split(' ',maxsplit=1)[1]
        reply = sendMessage(f'Searching for {search} in my Google Drive Database...', context.bot, update)

        LOGGER.info(f"Searching: {search}")
        
        gdrive = GoogleDriveHelper(None)
        msg, button = gdrive.drive_list(search)

        editMessage(msg,reply,button)

    except IndexError:
        sendMessage('send a search key along with command', context.bot, update)


list_handler = CommandHandler(BotCommands.ListCommand, list_drive)
msg_handler = MessageHandler(Filters.all, list_drive)
dispatcher.add_handler(msg_handler)
dispatcher.add_handler(list_handler)
