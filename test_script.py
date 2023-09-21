"""Test for main"""
import pandas as pd
import mylib.script as script


def test_read():
    """test function for read"""
    df1 = script.read_in_file(
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
    )
    assert isinstance(df1, pd.DataFrame), "Fail to read the csv file"
    return df1


def test_describe():
    "test function for descriptive statistics"
    df1 = script.summary_statistics(test_read())
    assert df1["year"]["min"] == 1921.0
    assert df1["ppf"]["count"] == 30962.0
    assert df1["ppf"]["min"] == 88.0


def test_plot():
    "test function for visualization plot"
    script.visualization(test_read())
    assert True, "Plot generation successed"
