from pyrogram.client import Client
from pyrogram import Client, filters
from config import api_id, api_hash, session, SUDO
from ABDUL import app
import os
import platform

x = platform
arch = x.architecture()
machine = x.machine()
pro = x.processor()
sys = x.system()
un = x.uname()
pb = x.python_build()
pv = x.python_version()

platform.machine()


@app.on_message(filters.command("ping"))
async def start(client, msg):
  await msg.reply_text(
      text=
      f"CHOCO VC USERBOT \n \n \n**Machine:** --{machine}--\n**Arch:** --{arch}--\n**Processor:** --{pro}--\n**System:** --{sys}--\n**Uname:** --{un}--\n**Python Build:** --{pb}--\n**Pyhton Version:** --{pv}--"
  )
