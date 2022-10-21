import argparse
import json
import pandas as pd

from config import PATH


def write_json(file: dict, filename: str) -> None:
    with open(filename, "w") as f:
        f.write(json.dumps(file, indent=4))


def create_json(dataframe=None) -> dict:
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


def get_columns_list_from_parsed_arguments(arguments):
    try:
        columns = arguments.fields.split(",")
    except Exception:
        columns = None

    return columns


def parse_arguments():
    arguments_required = {
        "--fields": "required fields from csv",
    }
    parser = argparse.ArgumentParser(prog="main.py", add_help=True)

    for key, value in arguments_required.items():
        parser.add_argument(key, type=str.lower, help=value, required=False)

    return parser.parse_args()


def main():
    arguments = parse_arguments()
    columns = get_columns_list_from_parsed_arguments(arguments)

    print(columns, type(columns))

    df = read_csv_from_remote_storage(path=PATH, columns=columns)
    json_file = create_json(dataframe=df)
    write_json(file=json_file, filename="out.json")


if __name__ == "__main__":
    main()
