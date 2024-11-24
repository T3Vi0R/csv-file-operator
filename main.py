import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Style

import pandas as pd


# Function to generate random codes
def generate_codes(length, quantity):
    chars = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz123456789'
    codes = []
    for _ in range(quantity):
        code = ''.join(random.choice(chars) for _ in range(length))
        codes.append(code)
    return codes


# Function to save codes to CSV using pandas
def save_codes_to_csv(file_path, codes):
    df = pd.DataFrame(codes, columns=['Code'])
    df.to_csv(file_path, index=False)


# Function to split CSV file using pandas
def split_csv(file_path, progress_bar, status_label):
    df = pd.read_csv(file_path)
    file_size = os.path.getsize(file_path)
    num_splits = file_size // (2 * 1024 * 1024) + 1  # 2MB per file

    rows_per_file = len(df) // num_splits + 1

    progress_bar['maximum'] = num_splits
    for i in range(num_splits):
        start = i * rows_per_file
        end = start + rows_per_file
        part_df = df.iloc[start:end]
        part_file_path = f"{file_path.rsplit('.', 1)[0]}_part_{i + 1}.csv"
        part_df.to_csv(part_file_path, index=False)
        progress_bar['value'] = i + 1
        status_label.config(text=f"Splitting part {i + 1} of {num_splits}")
        progress_bar.update()


# GUI application
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Code Generator and CSV Splitter")

        # Set fixed size
        self.geometry("350x250")
        self.resizable(False, False)

        # Apply some styling
        style = Style(self)
        self.configure(bg="lightgray")
        style.configure("TLabel", background="lightgray")
        style.configure("TButton", padding=(5, 5))
        style.configure("TEntry", padding=(5, 5))

        self.length_label = tk.Label(self, text="Length of codes:", background="lightgray")
        self.length_label.pack(padx=10, pady=1)
        self.length_entry = tk.Entry(self)
        self.length_entry.pack(padx=10, pady=1)

        self.quantity_label = tk.Label(self, text="Quantity of codes:", background="lightgray")
        self.quantity_label.pack(padx=10, pady=5)
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.pack(padx=10, pady=5)

        self.generate_button = tk.Button(self, text="Generate Codes", command=self.generate_codes)
        self.generate_button.pack(padx=10, pady=5)

        self.split_button = tk.Button(self, text="Split CSV", command=self.split_csv)
        self.split_button.pack(padx=10, pady=5)

        self.progress_bar = Progressbar(self, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress_bar.pack(padx=10, pady=3)

        self.status_label = tk.Label(self, text="", background="lightgray")
        self.status_label.pack(padx=10, pady=5)

    def generate_codes(self):
        try:
            length = int(self.length_entry.get())
            quantity = int(self.quantity_entry.get())
            codes = generate_codes(length, quantity)

            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if file_path:
                save_codes_to_csv(file_path, codes)
                messagebox.showinfo("Success", "Codes generated and saved successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for length and quantity.")

    def split_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.status_label.config(text="Splitting CSV...")
            self.progress_bar['value'] = 0
            split_csv(file_path, self.progress_bar, self.status_label)
            self.status_label.config(text="CSV file split successfully!")
            messagebox.showinfo("Success", "CSV file split successfully!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
