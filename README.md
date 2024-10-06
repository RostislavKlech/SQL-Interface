# SQL Interface with Tkinter

This Python script provides a graphical SQL interface for querying data from files like Excel, CSV, JSON, and TXT using Tkinter. The data is loaded into an in-memory SQLite database and can be queried using SQL commands directly within the application.

## Features

- Load data from `.xlsx`, `.csv`, `.json`, or `.txt` files.
- Display results of SQL queries in a table format with a vertical scrollbar for easy navigation.
- Supports interactive SQL querying directly in the application interface.

## Requirements

- Python 3.x
- Required Python libraries: `pandas`, `sqlite3`, `tkinter`, `openpyxl` (for `.xlsx` files).

## Installation

1. Make sure Python is installed on your system.
2. Install the necessary Python packages using pip:

   ```bash
   pip install pandas openpyxl
   ```

## Usage

To run the script, open your terminal and use the following command:

```bash
python SQL.py <file_name>
```

Replace `<file_name>` with the path to your data file (e.g., `data.xlsx`, `data.csv`, etc.).

### Example

```bash
python SQL.py data.xlsx
```

## Script Description

1. **Opening the File:** The script detects the file type based on its extension (`.xlsx`, `.csv`, `.json`, or `.txt`) and loads the data into a pandas DataFrame.
2. **Loading Data into SQLite:** The data is transferred to an in-memory SQLite database, making it available for SQL queries.
3. **Graphical Interface:** The Tkinter GUI allows users to enter SQL queries and view results in a table format with vertical scrolling.

Note that snake_case (or camelCase) names of columns are needed.  

## Handling Errors

- If the script is run without the required arguments, it will display a usage message and exit.
- If the file type is unsupported or if loading fails, the script will notify the user and exit.

## Limitations

- The script currently supports `.xlsx`, `.csv`, `.json`, and `.txt` files. Additional file formats may require modifications to the code.
- Data is stored in memory, which may affect performance with very large datasets.
