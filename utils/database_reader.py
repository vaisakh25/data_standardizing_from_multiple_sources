import sqlite3

def read_database_table(database_path, table_name):
    """
    Reads data from a database table and returns a list of dictionaries.
    Each dictionary represents a row in the database table, with the keys
    representing the column headers and the values representing the
    corresponding row values.
    """
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    headers = [column[0] for column in cursor.description]
    rows = []
    for row in cursor.fetchall():
        rows.append({headers[i]: row[i] for i in range(len(headers))})
    conn.close()
    return rows
