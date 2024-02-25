"""
text2text-generation model 'google/flan-t5-large' to answer on english question.
given context is not required.
"""

from transformers import pipeline
from src.data.data_management import save_to_json, read_json

if __name__ == '__main__':
    pipe = pipeline("text2text-generation", model="google/flan-t5-large")

    # Get my extracted data from other models in my project directory but not uploaded to GitHub.
    # This is just an arbitrary example, use your own examples.
    text = read_json("transcribe_output.json")
    print(text["transcription"][0]["text"])

    ukraine_question = "from the below text what Ukraine says"
    cnn_question = "what cnn can't do?"

    res = pipe(cnn_question+(text["transcription"][0]["text"]), max_length=50)
    print(res[0]["generated_text"])

    save_to_json(res[0], "text", "answer.json")
