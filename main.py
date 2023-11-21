# -*- coding: utf-8 -*-

import revpimodio2
from setup import N_CHAMBERS, PATH, TABLENAME
import waves
import pandas as pd
from openpyxl import load_workbook

def main():
    # load wave information from excel file
    wb = load_workbook(filename = PATH)
    sheet = wb['Sheet1']
    lookup_table = sheet.tables[TABLENAME]

    # Access the data in the table range
    data = sheet[lookup_table.ref]
    table_values = []
    column_labels = []
    row_labels = []

    # Loop through each row and get the values in the cells
    for i, row in enumerate(data):
        if i == 0:
            for label in row[1:]:
                column_labels.append(label.value)
        else:
            # get labels for each row
            row_labels.append(row[0].value)
            # Get a list of all columns in each row
            cells = []
            for cell in row[1:]:
                cells.append(cell.value)
            table_values.append(cells)

    # Create a pandas dataframe from the rows_list.
    # The first row is the column names
    df = pd.DataFrame(data=table_values, index=row_labels, columns=column_labels, dtype=float)

    # check if file contains information for all wave chambers
    if len(df.index) != N_CHAMBERS:
         raise ValueError("Table does not contain information for all chambers or for too many chambers!")

    # get number of wave sets specified in file and perform sanity check
    if len(df.columns) % 4 != 0:
           raise ValueError("Table contains incomplete wavesets! Length of columns must be multiple of 4.")

    # Create the RevPiModIO object
    rpi = revpimodio2.RevPiModIO(autorefresh=True)

    # cerate waveset
    waves.create_waveset(rpi, df.values)

    # close all valves again
    waves.clean_up(rpi)



if __name__ == "__main__":
    main()