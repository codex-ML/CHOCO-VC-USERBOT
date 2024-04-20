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


@app.on_message(filters.command("join"))
async def join(client, message):
         commands = message.text.split(maxsplit=1)
         if  len(commands) != 2:
           await message.reply_text("invalid command")
         print(commands)
         chat_id = commands[1]
         await pytg.play(chat_id,MediaStream("em.mp3",
          video_flags=MediaStream.Flags.IGNORE),)