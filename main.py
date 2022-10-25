import argparse
import json
import os
import pandas as pd

from config import PATH, FILENAME, DIR_NAME


def check_existing_json_file(filename: str = FILENAME) -> bool:
    if os.path.exists(f"{DIR_NAME}/{filename}"):
        return True

    try:
        os.makedirs(f"{DIR_NAME}")
    except FileExistsError:
        ...

    return False


def get_file_list(dir_name: str = DIR_NAME) -> list:
    files = os.listdir(dir_name)
    return sorted(files)


def save_json_file(file: dict, filename: str = FILENAME) -> None:
    with open(f"{DIR_NAME}/{filename}", "w") as f:
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
        columns = arguments.fields.split(",")
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

    print(check_existing_json_file())
    if check_existing_json_file():
        print(get_file_list())
    # print(get_file_list())
    arguments = parse_arguments()
    columns = get_columns_list_from_parsed_arguments(arguments=arguments)
    df = read_csv_from_remote_storage(path=PATH, columns=columns)
    json_file = create_json_file(dataframe=df)
    save_json_file(file=json_file)


if __name__ == "__main__":
    main()
