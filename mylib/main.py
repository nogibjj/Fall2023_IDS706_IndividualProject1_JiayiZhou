"""
Main cli or app entry point
"""
import sys
import pandas as pd
try:
    import lib
except ModuleNotFoundError:
    sys.path.insert(1, './mylib')
    import lib


def read_in_file(filename):
    """read in a file"""
    return lib.read_file(filename)


def summary_statistics(data1):
    """provide sumamry statistics to numeric type data"""
    return lib.describe_file(data1)


def generate_html(data1):
    """generate a html file for summary statistics"""
    lib.save_table_html(data1)


def visualization(data1):
    "Plotting relationship between two variables"
    lib.plot_file(data1)
    lib.save_figure(data1)


if __name__ == "__main__":
    df1 = read_in_file(
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
    )
    summary_table = summary_statistics(df1)
    visualization(df1)
    generate_html(df1)
