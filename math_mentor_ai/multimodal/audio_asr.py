import os
import shutil
import tempfile
import whisper
import imageio_ffmpeg

# Setup ffmpeg: Ensure 'ffmpeg.exe' is available in PATH
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
ffmpeg_dir = os.path.dirname(ffmpeg_exe)

if os.path.basename(ffmpeg_exe).lower() != "ffmpeg.exe":
    # Copy to a temp dir as ffmpeg.exe if not already named so
    temp_ffmpeg_dir = os.path.join(tempfile.gettempdir(), "math_mentor_ffmpeg")
    os.makedirs(temp_ffmpeg_dir, exist_ok=True)
    target_exe = os.path.join(temp_ffmpeg_dir, "ffmpeg.exe")
    
    # Only copy if missing or size differs (simple cache check)
    if not os.path.exists(target_exe) or os.path.getsize(target_exe) != os.path.getsize(ffmpeg_exe):
        shutil.copy(ffmpeg_exe, target_exe)
    
    os.environ["PATH"] = temp_ffmpeg_dir + os.pathsep + os.environ["PATH"]
else:
    os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ["PATH"]

model = whisper.load_model("base")

def transcribe_audio(audio_file):
    """
    Converts audio to text using Whisper
    """

    suffix = ".wav"
    if hasattr(audio_file, "name"):
        _, ext = os.path.splitext(audio_file.name)
        if ext:
            suffix = ext

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        if isinstance(audio_file, bytes):
            tmp.write(audio_file)
        else:
            tmp.write(audio_file.read())
        temp_path = tmp.name

    try:
        result = model.transcribe(temp_path)

        text = result.get("text", "").strip()

        confidence = 0.9 if len(text) > 5 else 0.4

        return {
            "text": text,
            "confidence": confidence
        }
    finally:
        os.remove(temp_path)
