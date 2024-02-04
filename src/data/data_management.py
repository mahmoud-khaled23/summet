import json
from datetime import datetime
import os.path


def read_json(filename):
    filepath = "../../data/extracted_text/"+filename
    with open(filepath, 'r') as file:
        data = json.load(file)

    return data


def init_json(data, data_name, filename):
    with open(filename, 'w') as file:
        json.dump({data_name: [data]}, fp=file, indent=4)


def add_to_json(data, data_name, filename):
    with open(filename, 'r+') as file:
        data_list = json.load(file)
        data_list[data_name].append(data)
        file.seek(0)

        json.dump(data_list, fp=file, indent=4)


def save_to_json(text, data_name, filename):
    filepath = "../../data/extracted_text/"+filename
    if not os.path.exists(filepath):
        init_json(text, data_name, filepath)
    else:
        add_to_json(text, data_name, filepath)


def get_audio(audio_name):
    audio_path = "../../data/audio_files/"
    return audio_path+audio_name

