import csv

def get_data_from_csv(file_path, row_index, column_index):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
            
        # Skip header row if exists
        next(reader, None)

        for current_row_index, row in enumerate(reader):
            if current_row_index == row_index:
                # Check if the specified column index is within the row
                if column_index < len(row):
                    return row[column_index]
                else:
                    # Handle an out of range parameter
                    print("Column index is out of range for the specified row.")
                    return None

# CSV path and position in data
file_path = 'FordAutos2023.csv'
row_index = 0
column_index = 1

data = get_data_from_csv(file_path, row_index, column_index)

if data is not None:
    print(f"Data at row {row_index} and column {column_index}: {data}")
