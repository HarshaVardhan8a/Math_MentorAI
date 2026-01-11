import os
import shutil
import tempfile
import whisper
import imageio_ffmpeg

# Setup ffmpeg: Ensure 'ffmpeg' (or 'ffmpeg.exe') is available in PATH
ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
ffmpeg_dir = os.path.dirname(ffmpeg_exe)

target_name = "ffmpeg.exe" if os.name == 'nt' else "ffmpeg"

if os.path.basename(ffmpeg_exe).lower() != target_name.lower():
    # Copy to a temp dir with the standard name ("ffmpeg" or "ffmpeg.exe")
    temp_ffmpeg_dir = os.path.join(tempfile.gettempdir(), "math_mentor_ffmpeg")
    os.makedirs(temp_ffmpeg_dir, exist_ok=True)
    target_path = os.path.join(temp_ffmpeg_dir, target_name)
    
    # Only copy if missing or size differs
    if not os.path.exists(target_path) or os.path.getsize(target_path) != os.path.getsize(ffmpeg_exe):
        shutil.copy(ffmpeg_exe, target_path)
    
    # Make sure it's executable on non-Windows
    if os.name != 'nt':
        os.chmod(target_path, 0o755)

    os.environ["PATH"] = temp_ffmpeg_dir + os.pathsep + os.environ["PATH"]
else:
    # It already has the correct name, just add its dir to PATH
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
