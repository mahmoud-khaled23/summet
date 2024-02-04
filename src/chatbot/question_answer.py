"""
Question-Answer BOT
simple questions on the given context
IN USE
"""
from transformers import pipeline
from src.data.data_management import read_json, save_to_json

pipe = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

context_example = "Abu trika is a professional football player"

res = pipe(question="who is abu trika?", context=context_example)
print(res["answer"])

save_to_json(res, "Answer", "QA_bot.json")

