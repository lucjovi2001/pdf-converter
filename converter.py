import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PyPDF2 import PdfReader
import os, time

# main window
root = TkinterDnD.Tk()
root.title("PDF Converter")

# widgets
output_dir = tk.StringVar()
output_file = tk.StringVar()
selected_file = tk.StringVar()
