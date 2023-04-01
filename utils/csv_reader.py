import csv

def read_csv_file(file_path):
    """
    Reads data from a CSV file and returns a list of dictionaries.
    Each dictionary represents a row in the CSV file, with the keys
    representing the column headers and the values representing the
    corresponding row values.
    """
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]
        return rows
