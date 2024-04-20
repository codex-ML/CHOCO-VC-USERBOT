from pyrogram.types import Message
from pyrogram import filters, errors, enums
from ABDUL import app
from pyrogram.errors.exceptions.flood_420 import FloodWait
from ABDUL.core.db import add_user, add_group, all_users, all_groups, users, groups, remove_user
import asyncio
from config import OWNER_ID,SUDO 


@app.on_message(filters.command(["stats", "users"], ["/", "!", ".", "?"]))
async def dbtool(_, m: Message):
  if m.from_user.id != OWNER_ID & SUDO :
    return await m.reply_text("`You Don't Have Enough Rights To Do This!`")
  xx = all_users()
  x = all_groups()
  tot = int(xx + x)
  await m.reply_text(text=f"""
📊 Chats Stats
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)
