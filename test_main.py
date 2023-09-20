"""Test for main"""
import pandas as pd
import mylib.main as main


def test_read():
    """test function for read"""
    df1 = main.read_in_file(
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
    )
    assert isinstance(df1, pd.DataFrame), "Fail to read the csv file"
    return df1


def test_describe():
    "test function for descriptive statistics"
    df1 = main.summary_statistics(test_read())
    assert df1[["describe", "year"]][4, 1] == 1921.0
    assert df1[["describe", "ppf"]][0, 1] == 30962.0
    assert df1[["describe", "ppf"]][4, 1] == 88.0


def test_plot():
    "test function for visualization plot"
    main.visualization(test_read())
    assert True, "Plot generation successed"
