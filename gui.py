import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from regression_engine import run_linear_regression, run_logistic_regression
from utils import load_file


class RegressionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Regression GUI")

        self.data = None
        self.column_dropdowns = {}
        self.column_roles = {}
        self.dropdown_vars = {}
        self.target_var = tk.StringVar()
        self.regression_type = tk.StringVar(value="linear")

        self.create_widgets()

    def create_widgets(self):
        # Frame with scrollbar
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(main_frame)
        scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Buttons
        tk.Button(self.scrollable_frame, text="Load File", command=self.load_file).pack(pady=10)
        tk.Label(self.scrollable_frame, text="Regression Type:").pack()
        tk.OptionMenu(self.scrollable_frame, self.regression_type, "linear", "logistic").pack()

        self.column_frame = tk.Frame(self.scrollable_frame)
        self.column_frame.pack(pady=10)

        tk.Label(self.scrollable_frame, text="Target Column:").pack()
        self.target_dropdown = ttk.Combobox(self.scrollable_frame, textvariable=self.target_var)
        self.target_dropdown.pack()

        tk.Button(self.scrollable_frame, text="Run Regression", command=self.run_regression).pack(pady=10)

        self.output_text = tk.Text(self.scrollable_frame, height=15, width=80)
        self.output_text.pack()

    def load_file(self):
        filepath = filedialog.askopenfilename()
        if not filepath:
            return
        try:
            self.data = load_file(filepath)
        except Exception as e:
            messagebox.showerror("File Error", f"Failed to load file: {e}")
            return

        self.setup_column_selectors()

    def setup_column_selectors(self):
        for widget in self.column_frame.winfo_children():
            widget.destroy()

        tk.Label(self.column_frame, text="Select column roles:").pack()

        self.dropdown_vars = {}

        for col in self.data.columns:
            frame = tk.Frame(self.column_frame)
            frame.pack(fill="x", padx=10)

            tk.Label(frame, text=col, width=20, anchor="w").pack(side="left")

            var = tk.StringVar(value="exclude")
            dropdown = tk.OptionMenu(frame, var, "categorical", "numerical", "exclude")
            dropdown.pack(side="left")

            self.dropdown_vars[col] = var

        self.target_dropdown['values'] = list(self.data.columns)

    def run_regression(self):
        if self.data is None:
            messagebox.showerror("Error", "No dataset loaded.")
            return

        target_col = self.target_var.get()
        if not target_col:
            messagebox.showerror("Error", "Please select a target column.")
            return

        cat_cols = [col for col, var in self.dropdown_vars.items() if var.get() == "categorical"]
        num_cols = [col for col, var in self.dropdown_vars.items() if var.get() == "numerical"]

        if self.regression_type.get() == "linear":
            result, y_true, y_pred = run_linear_regression(self.data, target_col, cat_cols, num_cols)
        else:
            result, y_true, y_pred = run_logistic_regression(self.data, target_col, cat_cols, num_cols)

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, result)

        self.plot_results(y_true, y_pred)

    def plot_results(self, y_true, y_pred):
        plt.figure(figsize=(6, 4))
        plt.scatter(range(len(y_true)), y_true, label="Actual", alpha=0.7)
        plt.scatter(range(len(y_pred)), y_pred, label="Predicted", alpha=0.7)
        plt.title("Actual vs. Predicted")
        plt.xlabel("Sample Index")
        plt.ylabel("Value")
        plt.legend()
        plt.tight_layout()
        plt.show()