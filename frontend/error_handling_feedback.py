```python
import tkinter as tk
from tkinter import messagebox

def show_progress_bar(progress):
    progress_bar = tk.Progressbar(orient="horizontal", length=100, mode="determinate")
    progress_bar.pack()
    progress_bar["value"] = progress

def show_success_notification(message):
    messagebox.showinfo("Success", message)

def show_error_message(error):
    messagebox.showerror("Error", error)

def update_progress_bar(progress):
    progress_bar["value"] = progress
    root.update_idletasks()

def clear_progress_bar():
    progress_bar["value"] = 0
    root.update_idletasks()

root = tk.Tk()
root.withdraw()
```