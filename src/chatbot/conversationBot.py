from transformers import pipeline
from src.data.data_management import save_to_json

pipe = pipeline("text2text-generation", model="google/flan-t5-large")

res = pipe("who is the founder of apple company", max_length=50)

print(res)

save_to_json(res[0], "text", "answer.json")

