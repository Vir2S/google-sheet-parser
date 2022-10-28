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
