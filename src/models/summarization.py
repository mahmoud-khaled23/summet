"""
use the facebook/bart-large-cnn
summarize the transcribed text
"""

from transformers import pipeline
from src.data.data_management import read_json, save_to_json


if __name__ == '__main__':
    pipe = pipeline("summarization", model="facebook/bart-large-cnn")

    text_json = read_json("from_asr.json")
    summarization_example = text_json["transcription"][0]["text"]
    print(summarization_example)

    res = pipe(summarization_example, min_length=50, do_sample=False)
    print(res)

    save_to_json(res[0], "summarization", "summarized_bls.json")

