from transformers import pipeline
from src.data.data_management import save_to_json, read_json

# too slow
# pipe = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")
audio_path = "../../data/audio_files/CNN_Report.mp3"


# res = pipe(audio_path)
# print(res)
# save_to_json(res, "transcription", "../../data/extracted_text/from_asr.json")

import openai
from openai import OpenAI

# openai.api_key = "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"

client = OpenAI(
    api_key="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"
)

audio_file = open(audio_path, "rb")

transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)

print(transcript)
print(transcript['choices'][0]['message']['content'])


