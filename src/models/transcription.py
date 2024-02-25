"""
automatic-speach-recognition model 'openai/whisper-base' to transcribe the given audio with speaker annotation
"""
from transformers import pipeline
from src.data.data_management import save_to_json, get_audio

if __name__ == '__main__':
    transcribe = pipeline(model="openai/whisper-base")

    # Get an audio example located in my project directory but not uploaded to GitHub.
    # This is just an arbitrary example, use your own examples.
    transcription_example = get_audio("CNN_Report.mp3")

    res = transcribe(transcription_example, generate_kwargs={"language": "english"})
    print(res)

    save_to_json(res, "transcription", "transcribe_output.json")
