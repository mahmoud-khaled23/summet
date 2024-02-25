"""
automatic-speach-recognition model 'openai/whisper-medium' to get the transcription in arabic from the audio file
"""

import tqdm
from transformers import pipeline
from src.data.data_management import save_to_json, get_audio


if __name__ == '__main__':
    transcribe = pipeline(model="openai/whisper-medium")

    # Get an audio example located in my project directory but not uploaded to GitHub.
    # This is just an arbitrary example, use your own examples.
    audio_ar_ex = get_audio("audio_ar_30s.mp3")

    res = transcribe(audio_ar_ex, generate_kwargs={"language": "arabic"})
    print(res)

    save_to_json(res, "transcription", "transcribe_ar.json")
