import pytest

import main


@pytest.mark.get_columns_from_parsed_arguments
def test_get_columns_list_from_parsed_arguments_with_str():
    arguments = "clicks,date"
    assert main.get_columns_list_from_parsed_arguments(arguments) == ["clicks", "date"]


@pytest.mark.get_columns_from_parsed_arguments
def test_get_columns_list_from_parsed_arguments_with_none():
    arguments = None
    assert main.get_columns_list_from_parsed_arguments(arguments) is None


@pytest.mark.get_columns_from_parsed_arguments
def test_get_columns_list_from_parsed_arguments_with_list():
    arguments = ["clicks", "date"]
    assert main.get_columns_list_from_parsed_arguments(arguments) is None


@pytest.mark.get_columns_from_parsed_arguments
def test_get_columns_list_from_parsed_arguments_with_tuple():
    arguments = ("clicks", "date")
    assert main.get_columns_list_from_parsed_arguments(arguments) is None


@pytest.mark.create_json_file
def test_create_json_file():
    dataframe = None
    assert main.create_json_file(dataframe) == {"data": []}


@pytest.mark.create_json_file
def test_create_json_file_with_data():
    dataframe = main.pd.read_csv("samples/sample.csv")
    with open("samples/sample.json", "r") as f:
        json_sample = main.json.loads(f.read()).get("data")
    assert main.create_json_file(dataframe) == {"data": json_sample}

