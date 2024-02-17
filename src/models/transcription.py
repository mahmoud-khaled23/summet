"""
The model to get the transcription from the audio file
IN USE
"""


import sys

sys.path.insert(0, '../../src')

from transformers import pipeline
from src.data.data_management import save_to_json, get_audio


if __name__ == '__main__':
    transcribe = pipeline(model="openai/whisper-base")
    transcription_example = get_audio("CNN_Report.mp3")

    res = transcribe(transcription_example, generate_kwargs={"language": "english"})
    print(res)

    save_to_json(res, "transcription", "transcribe_output.json")

