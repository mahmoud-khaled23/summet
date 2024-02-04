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


def file_size(fpath):
    fsize = os.stat("data/" + fpath)
    print(f'file size = {fsize.st_size / (1024 ** 2)} MB')
    return


def get_openai_token():
    """
    get openai api token from json file in path on my device, replace it with your filepath.
    The api token should be in my environment variables but there is a problem in my IDE.
    :return:
    """
    with open("/home/ma7moud-5aled/for_vscode/tokens.json", 'rb') as file:
        keys = json.load(file)

    my_summet_key = keys["TOKENS"]["Mahmoud"]
    # print(my_summet_key)
    return my_summet_key


def get_audio(audio_name):
    audio_path = "../../data/audio_files/"
    return audio_path+audio_name


def get_json_path(json_name):
    json_path = "../../data/extracted_text/"
    return json_path+json_name


def replicate_auth_token(token_name):
    with open("/home/ma7moud-5aled/for_vscode/tokens.json", 'rb') as file:
        keys = json.load(file)

    key = keys["TOKENS"][token_name]
    return key

