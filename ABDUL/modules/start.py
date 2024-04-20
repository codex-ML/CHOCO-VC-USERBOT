from pyrogram.client import Client
from pyrogram import Client, filters
from config import api_id, api_hash, session, SUDO
from ABDUL import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

@app.on_message(filters.command("start"))
async def handle_start_command(client, message):
  # send a reply to the user
  await message.reply("Hello, I'm a bot! How are you?")