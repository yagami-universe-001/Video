# Admin commands for Video Encoder Bot
import os
from pyrogram import Client, filters
from config import ADMINS

@Client.on_message(filters.command("update") & filters.user(ADMINS))
async def update(c,m):
    await m.reply_text("📦 Pulling latest...")
    out = os.popen("git pull 2>&1").read()
    await m.reply_text(f"✅ Update output:\n{out}")

@Client.on_message(filters.command("queue") & filters.user(ADMINS))
async def queue(c,m):
    await m.reply_text("🕒 Queue empty (coming soon).")
