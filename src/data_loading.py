import pandas as pd

# List of the file names
files = [
    'EPS1.txt', 'FS1.txt', 'FS2.txt', 'PS1.txt', 'PS2.txt', 'PS3.txt', 'PS4.txt', 'PS5.txt', 'PS6.txt',
    'SE.txt', 'TS1.txt', 'TS2.txt', 'TS3.txt', 'TS4.txt', 'VS1.txt'
]

# Initialize an empty list to hold the processed data
all_data = []

# Loop through the file list and process each file
for file in files:
    # Read the file using the 'python' engine to handle the space-separated values
    data = pd.read_csv(f'../data/raw/{file}', header=None, sep=r'\n', engine='python')
    
    # Flatten the list of rows (convert to a single column of values)
    data = data[0].str.split(expand=True).stack().reset_index(drop=True)
    
    # Convert the values to numeric type (if necessary)
    data = pd.to_numeric(data)
    
    # Add the data to the list
    all_data.append(data)

# Combine all the data into a single DataFrame
combined_data = pd.concat(all_data, axis=1)

# Define a list of column names corresponding to the physical quantities
column_names = [
    "Motor Power",        # EPS1
    "Volume Flow 1",      # FS1
    "Volume Flow 2",      # FS2
    "Pressure 1",         # PS1
    "Pressure 2",         # PS2
    "Pressure 3",         # PS3
    "Pressure 4",         # PS4
    "Pressure 5",         # PS5
    "Pressure 6",         # PS6
    "Efficiency Factor",  # SE
    "Temperature 1",      # TS1
    "Temperature 2",      # TS2
    "Temperature 3",      # TS3
    "Temperature 4",      # TS4
    "Vibration"           # VS1
]

# Rename columns
combined_data.columns = column_names

# Save the combined data to a CSV file
combined_data.to_csv('../data/processed/compiled_data.csv', index=False)

# Show the data
combined_data.head()