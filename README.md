## Fall2023_IDS706 Individual Project 1: Continuous Integration using GitHub Actions of Python Data Science Project
### by Jiayi Zhou
[![OnInstall](https://github.com/nogibjj/Fall2023_IDS706_IndividualProject1_JiayiZhou/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Fall2023_IDS706_IndividualProject1_JiayiZhou/actions/workflows/install.yml)
[![Test](https://github.com/nogibjj/Fall2023_IDS706_IndividualProject1_JiayiZhou/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Fall2023_IDS706_IndividualProject1_JiayiZhou/actions/workflows/test.yml)
[![Lint](https://github.com/nogibjj/Fall2023_IDS706_IndividualProject1_JiayiZhou/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Fall2023_IDS706_IndividualProject1_JiayiZhou/actions/workflows/lint.yml)
[![Format](https://github.com/nogibjj/Fall2023_IDS706_IndividualProject1_JiayiZhou/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Fall2023_IDS706_IndividualProject1_JiayiZhou/actions/workflows/format.yml)
### Purpose
This is for class data engineering individual project 1. It uses a Python Ruff GitHub template with pandas to run and test a function that provides summary statistics and data visualization. It utilizes continuous integration using GitHub Actions to automatically set up environment, test, format and lint code.

### Video
Here is the link for youtube: https://youtu.be/UqX_fCYPfbE
### Structure
1. `Jupyter Notebook(mylib/describe_file.ipynb)`:
  * Contains cells that perform descriptive statistics using Pandas.
  * Plot the figure data.
  * Validated using the nbval plugin for pytest.
2.  `Python Script(mylib/script.py)`:
  * Executes the descriptive statistics using Pandas.
  * Plot the figure of data.
3.  `Python Script(mylib/lib.py)`:
  * Holds shared code used by both the script and the notebook.
4. `test_script.py(test_script.py)`:
  * Contains tests for the Python script.
5. `test_lib.py(tests/test_lib.py)`:
  * Contains tests for the library.
6.  `Makefile`:
  * Contains four commands (Run by GitHub Workflows on each Push and Pull):
    * Test: Run all tests (notebook, script, and lib)
    * Format: Format code with Python black
    * Lint: Lint code with Ruff
    * Install: Install dependencies via pip install -r requirements.txt
7. `Pinned requirements.txt`:
  * Specifies exact versions of dependencies.

### Steps
I created the template based on the template created by Professor Noah Gift and modified the template. Based on the template from professor, I made the following changes:
1. Added pandas==2.1.0, matplotlib==3.7.3, nbqa==1.7.0, tabulate==0.9.0, jupyter==1.0.0 in `requirements.txt`
2. Modified `Makefile` to add jupyter notebook test.
3. Added functions in `lib.py` to read the CSV file, store and return the summary statistics table, create and save a plot with Pandas library.
4. Added the function in `script.py` to call functions in lib.py to read in dataset, store and return the summary statistics table, create and save a plot with Pandas library.
5. Added the function in `describe_file.ipynb` to call functions in `lib.py` to read in dataset, store and return the summary statistics table, create and save a plot with Pandas library.
6. Added test cases in `test_lib.py`
7. Added test cases in `test_script.py`

### Dataset
The dataset is loaded in based on url.  Here is the url: [(https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv)](https://raw.githubusercontent.com/fivethirtyeight/data/master/goose/goose_rawdata.csv). The file is a comma-separated value spreadsheet (CSV) called goose_rawdata.csv.  
<img width="497" alt="Screenshot 2023-09-12 at 10 19 05 PM" src="https://github.com/nogibjj/Fall2023_IDS706_MiniProject3_JiayiZhou/assets/143651921/ca45cc76-2d2e-4d26-a2b5-6bff9dcaf0ee">

### Result
Here is the screenshot of summary statistics table based on the csv file read in.  
<img width="702" alt="Screenshot 2023-09-20 at 12 47 26 AM" src="https://github.com/nogibjj/Fall2023_IDS706_IndividualProject1_JiayiZhou/assets/143651921/f5cf338a-61f1-42a9-893a-1f404b54e8d6">  
Here is the visualization between two variables in the dataframe, which can also be viewed by clicking on `YearGoose.png` under output folder.  
<img width="636" alt="Screenshot 2023-09-20 at 12 48 03 AM" src="https://github.com/nogibjj/Fall2023_IDS706_IndividualProject1_JiayiZhou/assets/143651921/5163f95d-bb74-4583-a961-2896959fdfab">
