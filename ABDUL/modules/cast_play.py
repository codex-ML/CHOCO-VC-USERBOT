import os
import time
import asyncio
import subprocess
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls.types import AudioQuality
from pytgcalls.types import VideoQuality
from config import session, api_id, api_hash
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import MediaStream
from pytgcalls.types import AudioQuality
from pytgcalls.types import VideoQuality
from config import api_id, api_hash, session, SUDO
from ABDUL import app, pytg


@app.on_message(filters.regex('.play'))
async def play_handler(_, message):
  replied_message = message.reply_to_message
  if not replied_message or not replied_message.audio:
    await message.reply_text("Reply to an audio message to play it.")
    return
  audio_file_path = f"{replied_message.audio.file_id}.ogg"
  # Download the audio using Pyrogram's download_media
  audio_file = await app.download_media(replied_message.audio)
  # Play the downloaded audio using ffplay
  await message.reply_text("downloaded done.")
  await pytg.play(
      message.chat.id,
      MediaStream(
          audio_file,
          # AudioQuality.HIGH,
          # video_flags=MediaStream.IGNORE,
          # VideoQuality.HD_720P,
      ),
  )
  await message.reply_text("stream end.")