import os
import asyncio
import importlib
import logging
import random
from pyrogram import idle
from pyrogram.client import Client
from ABDUL import app
from ABDUL.modules import ALL_MODULES
from pyrogram import filters, errors
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from pyrogram.errors import FloodWait, PeerIdInvalid
from config import *
from ABDUL import app
import subprocess
import shlex
from pyrogram.errors import FloodWait
import pymongo
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import Update
from pytgcalls.types import MediaStream
from pytgcalls.types import AudioQuality
from pytgcalls.types import VideoQuality

loop = asyncio.get_event_loop()


async def init():

  for all_module in ALL_MODULES:
    importlib.import_module("ABDUL.modules." + all_module)
    print(f"LOADING {all_module} ...")
  print(f"""\n
 ___  ___ _____      _            _          _ 
| _ )/ _ \_   _|  __| |_ __ _ _ _| |_ ___ __| |
| _ \ (_) || |   (_-<  _/ _` | '_|  _/ -_) _` |
|___/\___/ |_|   /__/\__\__,_|_|  \__\___\__,_|
""")

  await idle()


print(f"""\n
  ___           _     _                       
 |   \ ___ _ __| |___(_)_ _  __ _             
 | |) / -_) '_ \ / _ \ | ' \/ _` |  _   _   _ 
 |___/\___| .__/_\___/_|_||_\__, | (_) (_) (_)
          |_|               |___/             
""")

logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO
    format=
    '%(asctime)s - %(levelname)s - %(message)s',  # Define log message format
    filename='app.log',  # Log file name
    filemode='w')  # Set log file mode to 'write'

# Create a logger
logger = logging.getLogger()

# Log messages at different levels
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')





if __name__ == "__main__":
  loop.run_until_complete(init())
  print("Stopping Bot! GoodBye")
