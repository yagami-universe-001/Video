# Video Encoder Bot
# Telegram bot to encode and edit videos (Pyrogram + FFmpeg)

## Features
- Encode to multiple resolutions
- Thumbnail management
- Extract audio/subtitles
- Admin commands
- MongoDB integration

## Quick start
1. Copy `.env.template` → `.env` and fill values.
2. Install Python & FFmpeg.
3. Create venv, install deps: `pip install -r requirements.txt`.
4. Run: `python3 main.py`.

## Docker
Build: `docker build -t video-editor-bot .`
Run: `docker run -d --env-file .env video-editor-bot`
