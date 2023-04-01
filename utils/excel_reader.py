import openpyxl

def read_excel_file(file_path, sheet_name):
    """
    Reads data from an Excel file and returns a list of dictionaries.
    Each dictionary represents a row in the Excel sheet, with the keys
    representing the column headers and the values representing the
    corresponding row values.
    """
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    headers = [cell.value for cell in sheet[1]]
    rows = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        rows.append({headers[i]: row[i] for i in range(len(headers))})
    return rows
