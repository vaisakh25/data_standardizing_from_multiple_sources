def standardize_data(data):
    """
    Standardizes the data format across different sources.
    The input data should be a list of dictionaries, where each dictionary
    represents a row in the data source, with the keys representing the
    column headers and the values representing the corresponding row values.
    The output data will have the same column headers and data types across
    all sources.
    """
    standardized_data = []
    for row in data:
        standardized_row = {}
        for key, value in row.items():
            if isinstance(value, str):
                standardized_row[key] = value.strip()
            else:
                standardized_row[key] = value
        standardized_data.append(standardized_row)
    return standardized_data
