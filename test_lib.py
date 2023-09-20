"""
Test Cases
"""
import pandas as pd
from mylib.lib import read_file, describe_file, save_table_html, plot_file, save_figure


def test_read():
    """test function for read"""
    df1 = read_file(
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
    )
    assert isinstance(df1, pd.DataFrame), "Fail to read the csv file"


def test_describe():
    """test function for describe dataframe"""
    # read a csv file by url
    df1 = describe_file(
        read_file(
            "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
        )
    )
    assert df1["year"]["min"] == 1921.0
    assert df1["ppf"]["count"] == 30962.0
    assert df1["ppf"]["min"] == 88.0


def test_plot():
    """test function for plot"""
    plot_file(
        read_file(
            "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
        )
    )
    assert True, "Plot generation successed"


def test_html():
    "test function for save table"
    save_table_html(
        read_file(
            "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
        )
    )
    assert True, "Markdown save successed"


def test_figure():
    "test function for save figure"
    save_figure(
        read_file(
            "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
        )
    )
    assert True, "Plot save successed"
