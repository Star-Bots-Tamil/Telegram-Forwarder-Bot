from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, filters
from telegram.constants import ParseMode
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from forwarder import bot, OWNER_ID

START = """
<b>Hi 👋🏻 {},
I'm {} to Maintain Your Channels. I am very useful for the Channel Admin who have many Channels.

See /help for more Details.

Maintained By :- <a href='https://t.me/TG_Karthik'>Karthik</a></b>
"""

GROUP_START = """
<b>I'm Working Only PM</b>
"""

HELP = """
<b>Hi 👋🏻 {},

Here is a list of usable Commands :-
♦️ /start :- Check if 😊 I'm Alive
♦️ /forward :- to Request to add Source And Distinction Channels ID (Direct Request to Admin)
♦️ /help :- This Bot's Features 
♦️ /about :- to Know About Me 😁
♦️ /id :- Get Your 🆔

Just Send /id in Private Chat/Group/Channel and i will Reply it's ID.</b>
"""

ABOUT = """
<b>🤖 My Name : Star Auto Forward Bot

🧑🏻‍💻 Developer : Karthik

📝 Language : Pyrogram

📚 Framework : Python3

📡 Hosted on : VPS

📢 Updates Channel : @Star_Moviess_Tamil</b>
"""

FORWARD = """
<b>Hello 👋🏻 {}
Request You Forward Channels</b>
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    message = update.effective_message
    user = update.effective_user
    keyboard = [
        [
            InlineKeyboardButton("Update Channel", url="https://t.me/Star_Bots_Tamil"),
            InlineKeyboardButton("Add My Forwards", url="https://t.me/TG_Karthik")
        ]
    ]
    keyboard1 = [
        [
            InlineKeyboardButton("Check PM", url="https://t.me/Star_Auto_Forward_Bot"),
            InlineKeyboardButton("Add My Forwards", url="https://t.me/TG_Karthik")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if not (chat and message and user):
        return

    if chat.type == "private":
        await message.reply_text(
            START.format(user.first_name, context.bot.first_name),
            parse_mode=ParseMode.HTML,
            quote=True,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
    else:
        await message.reply_text(
            GROUP_START.format(user.first_name, context.bot.first_name),
            parse_mode=ParseMode.HTML,
            quote=True,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )

async def help(update: Update, _):
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    keyboard = [
        [
            InlineKeyboardButton("Update Channel", url="https://t.me/Star_Bots_Tamil"),
            InlineKeyboardButton("Add My Forwards", url="https://t.me/TG_Karthik")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if not (chat and message):
        return

    if not chat.type == "private":
        await message.reply_text("Contact me via PM to get a list of usable commands.")
    else:
        await message.reply_text(
            HELP.format(user.first_name, context.bot.first_name),
            parse_mode=ParseMode.HTML,
            quote=True,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    message = update.effective_message
    user = update.effective_user
    keyboard = [
        [
            InlineKeyboardButton("Update Channel", url="https://t.me/Star_Bots_Tamil"),
            InlineKeyboardButton("Add My Forwards", url="https://t.me/TG_Karthik")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if not (chat and message and user):
        return

    if chat.type == "private":
        await message.reply_text(
            ABOUT.format(user.first_name, context.bot.first_name),
            parse_mode=ParseMode.HTML,
        )
    else:
        await message.reply_text("About Me")

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat = update.effective_chat
    message = update.effective_message
    user = update.effective_user
    keyboard = [
        [
            InlineKeyboardButton("Update Channel", url="https://t.me/Star_Bots_Tamil"),
            InlineKeyboardButton("Add My Forwards", url="https://t.me/TG_Karthik")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if not (chat and message and user):
        return

    if chat.type == "private":
        await message.reply_text(
            FORWARD.format(user.first_name, context.bot.first_name),
            parse_mode=ParseMode.HTML,
        )
    else:
        await message.reply_text("Request Forward Files At PM")

bot.add_handler(CommandHandler("start", start))
bot.add_handler(CommandHandler("help", help))
bot.add_handler(CommandHandler("about", about))
bot.add_handler(CommandHandler("forward", forward))
