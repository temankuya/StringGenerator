import logging
from typing import Union
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from StringGen.save_user import save_user
from StringGen.database import users

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def command_filter(cmd: Union[str, list]) -> filters.Filter:
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(command_filter(["start", "help"]))
async def start_handler(bot: Client, message: Message):
    user = message.from_user
    await save_user(user)

    try:
        bot_info = await bot.get_me()
        bot_name = bot_info.first_name or "This Bot"

        existing = await users.find_one({"_id": user.id})
        join_info = ""
        if existing and "joined" in existing:
            join_time = existing["joined"]
            if isinstance(join_time, datetime):
                join_info = f"\n🕒 ʏᴏᴜ ᴊᴏɪɴᴇᴅ: **{join_time.strftime('%d-%m-%Y %I:%M %p')} IST**"

        response_text = (
            f"👋 ʜᴇʏ {user.mention},\n\n"
            f"ɪ ᴀᴍ **{bot_name}** — ᴀ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.\n"
            "ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴄʀᴇᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴꜱ ꜰᴏʀ **ᴘʏʀᴏɢʀᴀᴍ / ᴛᴇʟᴇᴛʜᴏɴ**, ᴜꜱᴇʀ ᴀɴᴅ ʙᴏᴛ ᴀᴄᴄᴏᴜɴᴛꜱ."
            f"{join_info}\n\n"
            "ᴛᴀᴘ **ʙᴇʟᴏᴡ** ᴛᴏ ʙᴇɢɪɴ ⬇️"
        )

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("⚙️ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴇꜱꜱɪᴏɴ", callback_data="generate")],
        ])

        await message.reply_text(
            text=response_text,
            reply_markup=keyboard,
            disable_web_page_preview=True
        )

    except Exception as e:
        logger.exception("⚠️ Error in /start or /help handler:")
        await message.reply_text(
            "⚠️ ᴀɴ ᴜɴᴇxᴘᴇᴄᴛᴇᴅ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀʀᴇᴅ. ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ."
        )
