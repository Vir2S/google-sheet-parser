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


def main():
    df = read_csv_from_remote_storage(path=PATH)
    json_file = create_json(dataframe=df)
    write_json(file=json_file, filename="out.json")


if __name__ == "__main__":
    main()
