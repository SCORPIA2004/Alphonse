import csv
import numpy as np
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def readDataIntoArr(filename):
    column1 = []
    column2 = []
    column3 = []
    # filename = input("Enter filename: ")
    # open a file dialog box
    # Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    # filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    # print(filename)

    if filename.endswith('.csv'):
        # Replace 'your_file.csv' with the actual file path
        column_arrays = []

        with open(filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)

            # Read the first row to get column names
            columns = next(csv_reader)

            # Initialize arrays for each column
            for _ in columns:
                column_arrays.append([])

            # Read and store data into arrays
            for row in csv_reader:
                for i, value in enumerate(row):
                    column_arrays[i].append(value)

    elif filename.endswith('.xlsx'):
        # Replace 'your_file.xlsx' with the actual file path
        data = pd.read_excel(filename)

        # Separate columns into arrays
        column_arrays = [data[column_name].tolist() for column_name in data.columns]
        # # Now each column's data is stored in a separate array in 'column_arrays'
        # column1 = column_arrays[0]
        # column2 = column_arrays[1]
        # column3 = column_arrays[2]

    # column1 = np.array(column1)
    # column2 = np.array(column2)
    # column3 = np.array(column3)
    # return column1, column2, column3
    return column_arrays
if __name__ == '__main__':
    columns = readDataIntoArr()
    print(columns)
    # c1, c2, c3 = readDataIntoArr()
    # print(c1)
    # print(c2)
    # print(c3)
