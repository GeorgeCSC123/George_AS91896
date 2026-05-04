import tkinter as tk
from tkinter import ttk

home = tk.Tk()
home.title("My App")

home.configure(bg="#7ed957")
label = tk.Label(home, text="Hello World",)
label.pack()

home.mainloop()

