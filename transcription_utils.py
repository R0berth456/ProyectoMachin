import os
import tempfile
import whisper
from pydub import AudioSegment

def transcribe_audio_segment(audio_path, start, end, model=None):
    if model is None:
        model = whisper.load_model("base")

    audio = AudioSegment.from_wav(audio_path)
    segment = audio[start * 1000:end * 1000]  # milisegundos

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        segment.export(tmp_file.name, format="wav")
        tmp_path = tmp_file.name

    result = model.transcribe(tmp_path, language="es")
    os.remove(tmp_path)
    return result["text"].strip()
