import argparse
import json
import os
import pandas as pd

from config import PATH, FILENAME, DIR_NAME


def get_file_list(dir_name: str = DIR_NAME) -> list:
    try:
        files = os.listdir(dir_name)
    except FileNotFoundError:
        os.makedirs(dir_name)
        files = []
    return sorted(files)


def save_json_file(file: dict, filename: str = None, dir_name: str = DIR_NAME) -> None:
    if filename is None:
        filename = FILENAME
    with open(f"{dir_name}/{filename}", "w") as f:
        f.write(json.dumps(file, indent=4))


def create_json_file(dataframe=None) -> dict:
    res = []
    if dataframe is None:
        return {
            "data": res
        }

    for index, row in dataframe.iterrows():
        res.append(dict(row))
    return {
        "data": res
    }


def read_csv_from_remote_storage(path: str = PATH, columns: list = None):
    return pd.read_csv(path, usecols=columns)


def get_columns_list_from_parsed_arguments(arguments) -> list or None:
    try:
        columns = arguments.split(",")
    except Exception:
        columns = None

    return columns


def parse_arguments():
    arguments_required = {
        "-fields": "required fields from csv",
        "-filename": "full path to file with filename and ext"
    }
    parser = argparse.ArgumentParser(prog="main.py", add_help=True)

    for key, value in arguments_required.items():
        parser.add_argument(key, type=str.lower, help=value, required=False)

    return parser.parse_args()


def main():

    print(get_file_list())
    arguments = parse_arguments()
    columns = get_columns_list_from_parsed_arguments(arguments=arguments.fields)
    df = read_csv_from_remote_storage(path=PATH, columns=columns)
    json_file = create_json_file(dataframe=df)
    save_json_file(file=json_file, filename=arguments.filename)


if __name__ == "__main__":
    main()
