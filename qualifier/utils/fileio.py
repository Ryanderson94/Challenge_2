# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data
    
# Function to save csv
def save_csv(save_csvpath, qualifying_loans, header):
    
    with open(Path(save_csvpath), 'w', newline='') as csvfile:
        # Create csv writer
        csvwriter = csv.writer(csvfile, delimiter=",")

        # Write header to csv file
        csvwriter.writerow(header)

        # Write values of each loan inside qualifying loans as row in the csv file
        for row in qualifying_loans:
            csvwriter.writerow(row)