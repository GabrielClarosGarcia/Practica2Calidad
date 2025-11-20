"""Setting setting.json file as user settings."""


import json
from os import listdir


def is_file_exist():
    if "setting.json" in listdir():
        return True
    else:
        False


def create_default_data():
    data = {
        "currency": "Reals",
        "data_file": "expense.csv",
    }

    with open("setting.json", mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return data


def load_conf():
    with open("setting.json", "r", encoding="utf-8") as file:
        setting = json.load(file)
    return setting


def configure():
    if is_file_exist():
        return load_conf()
    else:
        return create_default_data()


if __name__ == "__main__":
    configure()
