from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import filters, MessageHandler
from forwarder import OWNER_ID, bot

async def get_id(update: Update, _):
    message = update.effective_message
    chat = update.effective_chat
    if not message or not chat:
        return

    if chat.type == "private":  # Private chat with the bot
        return await message.reply_text(f"<b>💁🏻 Your ID is</b> <code>{chat.id}</code>", parse_mode=ParseMode.HTML)

    result = f"<b>👥 Chat ID :-</b> <code>{chat.id}</code>", parse_mode=ParseMode.HTML
    if chat.is_forum:
        result += f"<b>\n💬 Forum/Topic ID :-<b> <code>{message.message_thread_id}</code>", parse_mode=ParseMode.HTML

    if message.reply_to_message:
        forwarder = message.reply_to_message.from_user
        if message.reply_to_message.forward_from:  # Forwarded user
            sender = message.reply_to_message.forward_from
            result += f"<b>💁🏻 The Original Sender ({sender.first_name}), ID is :-</b> <code>{sender.id}</code>\n", parse_mode=ParseMode.HTML
            result += f"<b>⏩ The Forwarder ({forwarder.first_name if forwarder else 'Unknown'}) ID :-</b> <code>{forwarder.id if forwarder else 'Unknown'}</code>", parse_mode=ParseMode.HTML

        if message.reply_to_message.forward_from_chat:  # Forwarded channel
            channel = message.reply_to_message.forward_from_chat
            result += f"<b>💬 The Channel {channel.title} ID :-</b> <code>{channel.id}</code>\n", parse_mode=ParseMode.HTML
            result += f"<b>⏩ The Forwarder ({forwarder.first_name if forwarder else 'Unknown'}) ID :-</b> <code>{forwarder.id if forwarder else 'Unknown'}</code>", parse_mode=ParseMode.HTML

    return await message.reply_text(
        result,
        parse_mode=ParseMode.HTML,
    )


GET_ID_HANDLER = MessageHandler(
    filters.COMMAND & filters.Regex(r"^/id") & (filters.User(OWNER_ID) | filters.ChatType.CHANNEL),
    get_id,
)

bot.add_handler(GET_ID_HANDLER)
