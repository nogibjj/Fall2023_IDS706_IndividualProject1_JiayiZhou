"""Basic function goes here"""
import pandas as pd
import matplotlib.pyplot as plt


def read_file(input1):
    """Read a file"""
    try:
        data = pd.read_csv(input1)
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None
    except Exception as error:
        print(f"Error while loading CSV File: {str(error)}")
        return None

def describe_file(dataframe):
    """Describe the data frame"""
    summary_statistics = dataframe.describe()
    return summary_statistics


def plot_file(dataframe):
    """Plot relationship in a dataframe"""
    plt.scatter(dataframe["year"], dataframe["gwar"])
    plt.title("Start year of season vs Goose Wins Above Replacement")
    plt.xlabel("Start year of season")
    plt.ylabel("Goose Wins Above Replacement")

def save_figure(dataframe):
    # Save the plot as a figure
    plot_file(dataframe).savefig("Year vs Goose.png")

def main():
    """Main function to run the functions"""
    data1 = "https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv"
    # read dataset
    df1 = read_file(data1)
    print(df1)

    # compute summary statistics
    df2 = describe_file(df1)
    print(df2)

    # generate plot
    plot_file(df1)


if __name__ == "__main__":
    main()
