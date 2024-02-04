"""
The model to get the transcription from the audio file
IN USE
"""
from transformers import pipeline
from src.data.data_management import save_to_json, get_audio

transcribe = pipeline(model="openai/whisper-base")
transcription_example = get_audio("CNN_Report.mp3")

res = transcribe(transcription_example)
print(res)

save_to_json(res, "transcription", "transcribe_output.json")
