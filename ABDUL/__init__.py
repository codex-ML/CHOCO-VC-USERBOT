import os
from ABDUL.core.db import add_user, add_group, all_users, all_groups, users, remove_user
from pytgcalls import PyTgCalls, idle
from pyrogram.client import Client
from config import api_id, api_hash, session

print("starting pyro client...")
app = Client("userbot",
             api_id=api_id,
             api_hash=api_hash,
             session_string=session)

print("Py-tgcall....")
pytg = PyTgCalls(app)
pytg.start()

print("Py-tgcall started")
