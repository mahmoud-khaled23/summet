import json
from datetime import datetime
import os.path
# from mutagen.mp3 import MP3

now = datetime.now()


def read_json(filename):
    with open(filename, 'r') as file:
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
    if not os.path.exists(filename):
        init_json(text, data_name, filename)
    else:
        add_to_json(text, data_name, filename)


def file_size(fpath):
    fsize = os.stat("data/" + fpath)
    print(f'file size = {fsize.st_size / (1024 ** 2)} MB')
    return

