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


@app.on_message(filters.regex(".sjoin"))
async def join(client, message):
  await message.reply_text(text="joined")
  await pytg.play(
      message.chat.id,
      MediaStream("em.mp3", video_flags=MediaStream.Flags.IGNORE),
  )
