import csv
import sqlite3

def write_data_to_csv(data, file_path):
    """
    Writes the data to a CSV file.
    The input data should be a list of dictionaries, where each dictionary
    represents a row in the data source, with the keys representing the
    column headers and the values representing the corresponding row values.
    """
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)