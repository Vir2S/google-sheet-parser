import pandas as pd

URL = "https://drive.google.com/file/d/1zLdEcpzCp357s3Rse112Lch9EMUWzMLE/view"
PATH = f"https://drive.google.com/uc?id={URL.split('/')[-2]}"


def read_csv_from_remote_storage():
    df = pd.read_csv(PATH)
    print(df.values, len(df.values))
    return df.values


def main():
    print(read_csv_from_remote_storage())


if __name__ == "__main__":
    main()
