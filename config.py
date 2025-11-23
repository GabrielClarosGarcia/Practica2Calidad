"""Setting setting.json file as user settings."""


import json
from os import listdir


def is_file_exist():
    """Check if the json file setting file exists."""
    if "setting.json" in listdir():
        return True
    else:
        return False


def create_default_data():
    """Creates default data for setting file. It will create the file if it doesn't exist."""
    data = {
        "currency": "Reals",
        "datafile": "expense.csv",
    }

    with open("setting.json", mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return data


def load_conf():
    """Will load the data of setting file. Json file should exist."""
    with open("setting.json", "r", encoding="utf-8") as file:
        setting = json.load(file)
    return setting


def configure():
    """Main function that returns the setting file data as a dictionary.
    This can be used directly in code to get the data and don't need to use others directly to get data.
    """
    if is_file_exist():
        return load_conf()
    else:
        return create_default_data()


def change_setting(parameter, value):
    """Changes data of setting.json file as input values."""
    setting = configure()

    if parameter in ["currency", "datafile"]:
        if parameter == "currency":
            setting["currency"] = value
        elif parameter == "datafile":
            if not check_file_name(str(value)):
                return False
            setting["datafile"] = value

        write_changes(setting)
        return True
    else:
        return False


def check_file_name(file_name: str):
    """Checks if the csv file name is in a correct format."""
    if file_name[-4:] == ".csv":
        return True
    else:
        return False

def write_changes(changed_data):
    """Write changes of settings in the setting.json file."""
    with open("setting.json", mode="w", encoding="utf-8") as file:
        json.dump(changed_data, file, indent=4)
