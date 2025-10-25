# Configuration for Video Encoder Bot
import os
from dotenv import load_dotenv
load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
FFMPEG_PATH = os.getenv("FFMPEG_PATH", "/usr/bin/ffmpeg")
FFPROBE_PATH = os.getenv("FFPROBE_PATH", "/usr/bin/ffprobe")
SESSION_NAME = os.getenv("SESSION_NAME", "VideoEncoderBot")
ADMINS = [OWNER_ID] if OWNER_ID else []
