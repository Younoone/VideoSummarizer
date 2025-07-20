import os
import yt_dlp
import whisper
# --- Functions ---
# --- FIX: Removed caching from this function to ensure new URLs are always downloaded ---

# --- Constants ---
AUDIO_FILENAME = "audio.mp3"

def download_audio(youtube_url, output_path=AUDIO_FILENAME):
    if os.path.exists(output_path):
        os.remove(output_path)
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}],
        'postprocessor_args': ['-ar', '16000'],
        'quiet': False,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    if not os.path.exists(output_path):
        raise FileNotFoundError(f"Expected output file `{output_path}` not found.")
    return output_path

# --- FIX: Removed caching from this function to prevent stale results ---
def transcribe_audio(model_type, file_path=AUDIO_FILENAME):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    model = whisper.load_model(model_type)
    result = model.transcribe(file_path)
    return result["text"], result["language"]