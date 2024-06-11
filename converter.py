import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PyPDF2 import PdfReader
import os, time

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF", "*.pdf"), ("All", "*.*")])
    if file_path:
        selected_file.set(file_path)
       
# drag and drop function 
def drop(event):
    file_path = event.data
    if file_path.startwith("{") and file_path.endswith("}"):
        file_path = file_path[1:-1]
    selected_file.set(file_path)

def choose_dir():
    pass

def start_conversion():
    pass

# main window
root = TkinterDnD.Tk()
root.title("PDF Converter")

# register drag and drop
root.drop_taret_register(DND_FILES)
root.dnd_bind("<<Drop>>", drop)

# widgets
output_dir = tk.StringVar()
output_file = tk.StringVar()
selected_file = tk.StringVar()

tk.Label(root, text="Output Directory").pack()
tk.Entry(root, textvariable=output_dir).pack()
tk.Button(root, text="Browse", command=choose_dir).pack()

tk.Label(root, text="Output File").pack()
tk.Entry(root, textvariable=output_file).pack()

tk.Label(root, text="Select PDF File").pack()
tk.Entry(root, textvariable=selected_file, state="readonly").pack()

open_button = tk.Button(root, text="Open PDF", command=open_file)
open_button.pack()

convert_button = tk.Button(root, text="Convert", command=start_conversion)
convert_button.pack()

root.mainloop()