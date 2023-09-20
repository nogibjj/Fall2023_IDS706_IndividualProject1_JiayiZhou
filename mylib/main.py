"""
Main cli or app entry point
"""

from lib import read_file, describe_file, save_table_html, plot_file, save_figure


def read_in_file(filename):
    """read in a file"""
    return read_file(filename)


def summary_statistics(data1):
    """provide sumamry statistics to numeric type data"""
    return describe_file(data1)


def generate_html(data1):
    """generate a html file for summary statistics"""
    save_table_html(data1)


def visualization(data1):
    "Plotting relationship between two variables"
    plot_file(data1)
    save_figure(data1)


if __name__ == "__main__":
    df1 = read_in_file(
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
    )
    summary_table = summary_statistics(df1)
    visualization(df1)
    generate_html(df1)
