# User commands for Video Encoder Bot
from pyrogram import Client, filters
from utils.db import MongoDB
db=MongoDB()

@Client.on_message(filters.command("setthumb") & filters.reply)
async def set_thumb(c,m):
    if not m.reply_to_message or not (m.reply_to_message.photo or m.reply_to_message.document):
        return await m.reply_text("Reply to image to set thumbnail.")
    file_id = m.reply_to_message.photo.file_id if m.reply_to_message.photo else m.reply_to_message.document.file_id
    await db.set_thumb(m.from_user.id,file_id)
    await m.reply_text("✅ Thumbnail saved.")

@Client.on_message(filters.command("getthumb"))
async def get_thumb(c,m):
    thumb = await db.get_thumb(m.from_user.id)
    if not thumb: return await m.reply_text("❌ No thumbnail set.")
    await m.reply_photo(thumb, caption="Your thumbnail.")

@Client.on_message(filters.command("delthumb"))
async def del_thumb(c,m):
    await db.del_thumb(m.from_user.id)
    await m.reply_text("🗑️ Thumbnail deleted.")
