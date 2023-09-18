from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, filters
from telegram.constants import ParseMode

from forwarder import bot, OWNER_ID

PM_START_TEXT = """
<b>Hi 👋🏻 {},

I'm {} to Maintain Your Channels. I am very useful for the Channel Admin who have many Channels.

See /help for more Details.

Maintained By :- <a href='tg://user?id={OWNER_ID}'>Karthik</a></b>
"""

PM_HELP_TEXT = """
<b>Hi 👋🏻 {},

Here is a list of usable Commands :-
♦️ /start :- Check if 😊 I'm Alive
♦️ /forward :- to Request to add Source And Distinction Channels ID (Direct Request to Admin)
♦️ /help :- This Bot's Features 
♦️ /about :- to Know About Me 😁
♦️ /id :- Get Your 🆔

Just Send /id in Private Chat/Group/Channel and i will Reply it's ID.</b>
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    message = update.effective_message
    user = update.effective_user
    if not (chat and message and user):
        return

    if chat.type == "private":
        await message.reply_text(
            PM_START_TEXT.format(user.first_name, context.bot.first_name),
            parse_mode=ParseMode.HTML,
        )
    else:
        await message.reply_text("I'm up and running!")


async def help(update: Update, _):
    chat = update.effective_chat
    message = update.effective_message
    if not (chat and message):
        return

    if not chat.type == "private":
        await message.reply_text("Contact me via PM to get a list of usable commands.")
    else:
        await message.reply_text(PM_HELP_TEXT)


bot.add_handler(CommandHandler("start", start, filters=filters.User(OWNER_ID)))
bot.add_handler(CommandHandler("help", help, filters=filters.User(OWNER_ID)))
