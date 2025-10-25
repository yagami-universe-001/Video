# FFmpeg utilities for Video Encoder Bot
import asyncio, os, ffmpeg
from config import FFMPEG_PATH

quality_map = {"144p":"256x144","240p":"426x240","360p":"640x360","480p":"854x480","720p":"1280x720","1080p":"1920x1080","2160p":"3840x2160"}

async def encode_video(input_path:str, quality:str, output_dir:str=".")->str:
    resolution = quality_map.get(quality,"1280x720")
    base = os.path.splitext(os.path.basename(input_path))[0]
    out_path = os.path.join(output_dir,f"{base}_{quality}.mp4")
    def _run():
        ffmpeg.input(input_path).output(out_path,vf=f"scale={resolution}",vcodec="libx264",crf=28,preset="medium",acodec="aac",audio_bitrate="128k").overwrite_output().run(cmd=FFMPEG_PATH,capture_stdout=False,capture_stderr=False)
    await asyncio.to_thread(_run)
    return out_path
