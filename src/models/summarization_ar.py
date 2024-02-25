"""
text2text-generation model 'malmarjeh/mbert2mbert-arabic-text-summarization' to summarize arabic text
"""
from src.data.data_management import read_json, save_to_json

from transformers import BertTokenizer, AutoModelForSeq2SeqLM, pipeline
from arabert.preprocess import ArabertPreprocessor


if __name__ == '__main__':
    model_name = "malmarjeh/mbert2mbert-arabic-text-summarization"
    preprocessor = ArabertPreprocessor(model_name="")

    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    pipeline = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

    textfile = read_json("transcribe_ar.json")
    text_ar = textfile["transcription"][-1]["text"]
    print(text_ar)
    text_ar = preprocessor.preprocess(text_ar)

    result = pipeline(text_ar,
                      eos_token_id=tokenizer.eos_token_id,
                      num_beams=3,
                      repetition_penalty=3.0,
                      max_length=200,
                      length_penalty=1.0,
                      no_repeat_ngram_size=3)[0]

    print(result)

    save_to_json(result, "summarized", "summarization_ar.json")
