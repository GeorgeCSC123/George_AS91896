
import tkinter as tk

#main window sizing and bg colour
root = tk.Tk()
root.title("My App")
root.geometry("900x600")
root.configure(bg="#7ed957")

#creating title
title_label = tk.Label(root, text="George’s countries quiz", fg="white", bg="#7ed957", font=("arial",50, "bold"))

#creating image and displaying
photo = tk.PhotoImage(file=r"C:\Users\23068\OneDrive - Mt Roskill Grammar School\Documents\Screenshot 2026-05-19 091556.png")
photo_label = tk.Label(root, image=photo, bg="#7ed957")

#creating start quiz button
start_button = tk.Button(root, text="Start Quiz", font=("Arial", 30, "bold"), fg="#7ed957", bg="black")
start_button.pack(side=tk.BOTTOM, pady=30)

#postioning of widgets
title_label.pack(pady=30)
photo_label.pack(pady=30)

#keeps window running
root.mainloop()

