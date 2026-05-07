import tkinter as tk


root = tk.Tk()
root.title("My App")
root.geometry("400x300")
root.configure(bg="#7ed957")
title_label = tk.Label(root, text="George’s countries quiz", fg="white", bg="#7ed957", font=("arial", 20, "bold"))

photo = tk.PhotoImage(file="image1.png")
photo_label = tk.Label(root, image=photo)

title_label.pack(pady=20)
photo_label.pack(pady=20)

root.mainloop()
