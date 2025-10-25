# Video encoding commands for Video Encoder Bot
import os
from pyrogram import Client, filters
from utils.ffmpeg_utils import encode_video

@Client.on_message(filters.command(["144p","240p","360p","480p","720p","1080p","2160p"]) & filters.reply)
async def encode_cmd(c,m):
    quality = m.command[0]
    if not m.reply_to_message or not (m.reply_to_message.video or m.reply_to_message.document):
        return await m.reply_text("Reply to a video to encode.")
    status = await m.reply_text(f"⚙️ Encoding to {quality} ...")
    input_path = await m.reply_to_message.download()
    try:
        output_path = await encode_video(input_path, quality)
        await m.reply_video(output_path, caption=f"✅ Encoded to {quality}!")
    except Exception as e:
        await m.reply_text(f"❌ Encoding failed: {e}")
    finally:
        if os.path.exists(input_path): os.remove(input_path)
        if os.path.exists(output_path): os.remove(output_path)
        await status.delete()
