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
from ABDUL import app

@app.on_message(filters.regex('volume (\d+)'))
async def vol(client, message):
    volume_level = int(message.matches[0].group(1))
    await pytg.change_volume_call(
        message.chat.id,
        volume_level
    )