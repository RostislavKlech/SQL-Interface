import sqlite3
import pandas as pd
import tkinter as tk
import sys
from tkinter import ttk, messagebox

def open_file(file_name: str):
    file_format = file_name.split(".")[-1].lower()
    try:
        if file_format == "xlsx":
            df = pd.read_excel(file_name)
        elif file_format == "csv":
            df = pd.read_csv(file_name)
        elif file_format == "json":
            df = pd.read_json(file_name)
        elif file_format == "txt":
            df = pd.read_csv(file_name, delimiter=None)
        else:
            raise ValueError(f"Unsupported type: .{file_format}")
        return df
    except Exception as e:
        print(f"Error occurred: {e}")
        return None 

def execute_query():
    query = query_entry.get("1.0", tk.END).strip()  
    try:
        result = pd.read_sql_query(query, conn)
        update_table(result)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

def update_table(df):
    for row in table.get_children():
        table.delete(row)
    
    table["columns"] = list(df.columns)
    table["show"] = "headings"

    for col in df.columns:
        table.heading(col, text=col)
        table.column(col, anchor='center', stretch=True)

    for index, row in df.iterrows():
        table.insert("", "end", values=list(row))

if len(sys.argv) != 2:
    print("Usage: python SQL.py <file_name>")
    sys.exit(1)

file_name = sys.argv[1]
conn = sqlite3.connect(":memory:")
df = open_file(file_name)

if df is not None:
    df.to_sql(file_name.split(".")[0], conn, if_exists="replace", index=False)
else:
    sys.exit(1)

root = tk.Tk()
root.title(f"SQL Interface - Data frame: {file_name.split('.')[0]}")

query_label = tk.Label(root, text="SQL query:")
query_label.pack(padx=10, pady=5)

query_entry = tk.Text(root, height=15, width=80)
query_entry.pack(padx=10, pady=5)

execute_button = tk.Button(root, text="Run", command=execute_query)
execute_button.pack(padx=10, pady=5)

table_frame = tk.Frame(root)
table_frame.pack(padx=10, pady=5, expand=True, fill='both')
table = ttk.Treeview(table_frame)
y_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=y_scrollbar.set)
y_scrollbar.pack(side="right", fill="y")
table.pack(side="top", fill="both", expand=True)
root.mainloop()

conn.close()



