import openai
from openai import OpenAI
import os
from src.data.data_management import read_json, save_to_json

openai.api_key = os.environ.get("OPENAI_API_KEY")
print(openai.api_key)

openai.api_key = "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"

# chat_completion = openai.completions.create(
#     model="gpt-3.5-turbo-instruct",
#     # messages=[{"role": "user", "content": "Hello world"}],
#     prompt="Write a tagline for an ice cream shop."
# )

# print(chat_completion)
# print(chat_completion['choices'][0]['message']['content'])

client = OpenAI(
    api_key="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"
)

# text = read_json("../../data/extracted_text/from_asr.json")
text = read_json("/home/ma7moud-5aled/PycharmProjects/NLP/transcribeMeet/Speaker_Diarization/transcribe_output.json")


to_summarize = text["transcription"][-1]["text"]

to_summarize = to_summarize[:16380]

response = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  response_format={"type": "json_object"},
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "summarize the next text"+to_summarize}
  ]
)

print(response.choices[0].message.content)

save_to_json(response.choices[0].message.content, "text", "../../data/extracted_text/from_openai.json")
