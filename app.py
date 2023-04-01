import yaml
from utils.csv_reader import read_csv_file
from utils.excel_reader import read_excel_file
from utils.database_reader import read_database_table
from utils.data_standardizer import standardize_data
from utils.data_writer import write_data_to_csv

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

data = []
for source_config in config['data_sources']:
    source_type = source_config['name']
    if source_type == 'csv':
        file_path = source_config['file_path']
        source_data = read_csv_file(file_path)
    elif source_type == 'excel':
        file_path = source_config['file_path']
        sheet_name = source_config['sheet_name']
        source_data = read_excel_file(file_path, sheet_name)
    elif source_type == 'database':
        database_path = source_config['database_path']
        table_name = source_config['table_name']
        source_data = read_database_table(database_path, table_name)
    else:
        raise ValueError(f"Unknown data source type: {source_type}")
    data.extend(source_data)

standardized_data = standardize_data(data)

write_data_to_csv(standardized_data, 'output.csv')
