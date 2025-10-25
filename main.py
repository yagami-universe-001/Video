# Main entry for Video Encoder Bot
import os, asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID

app = Client("VideoEncoderBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="handlers"))

@app.on_message(filters.command("start"))
async def start_handler(_, message):
    name = message.from_user.first_name if message.from_user else "there"
    await message.reply_text(f"👋 Hello {name}!\nI’m a Video Editing Bot 🎬\nUse /help for commands.")

@app.on_message(filters.command("help"))
async def help_handler(_, message):
    await message.reply_text("User cmds: /setthumb /getthumb /delthumb /compress /merge /cut /crop /144p ...\nAdmin cmds: /restart /queue /clear /update")

@app.on_message(filters.command("restart") & filters.user(OWNER_ID))
async def restart(_, message):
    await message.reply_text("♻️ Restarting...")
    await asyncio.sleep(1)
    os.execv(sys.executable, [sys.executable]+sys.argv)

if __name__=="__main__":
    print("✅ Video Encoder Bot Started")
    app.run()
