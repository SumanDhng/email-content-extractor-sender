import pandas as pd
import json

# Convert data into json
def convert_to_json(data, file_path):
    json.dump(data, open(file_path, 'w'), indent=4)

# Load json from file
def load_json(file_path):
    return json.load(open(file_path, 'r'))

# Convert data to xlsx
def convert_to_xls(json_data, file_path):
    df = pd.DataFrame.from_dict(json_data)
    df.to_excel(file_path, index=False)

# load xlsx from file into dataframe
def load_xls(file_path):
    return pd.read_excel(file_path)