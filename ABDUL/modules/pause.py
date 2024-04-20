import os
import time
import asyncio
import subprocess
from pyrogram import Client, filters
from pyrogram.types import Message
from config import session, api_id, api_hash
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import MediaStream
from pytgcalls.types import AudioQuality
from pytgcalls.types import VideoQuality
from config import api_id, api_hash, session, SUDO
from ABDUL import app, pytg


@app.on_message(filters.regex('.pause'))
async def pause_handler(_: Client, message: Message):
  await message.reply_text(text="Userbot  paused song")
  await pytg.pause_stream(message.chat.id, )
