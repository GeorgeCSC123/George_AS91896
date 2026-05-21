
import tkinter as tk

root = tk.Tk()
root.title("My App")
root.geometry("400x300")
root.configure(bg="#7ed957")

title_label = tk.Label(root, text="George’s countries quiz", fg="white", bg="#7ed957", font=("arial",30, "bold"))

photo = tk.PhotoImage(file=r"C:\Users\23068\OneDrive - Mt Roskill Grammar School\Documents\Screenshot 2026-05-19 091556.png")
photo_label = tk.Label(root, image=photo, bg="#7ed957")

start_button = tk.Button(root, text="Start Quiz", font=("Arial", 14), fg="#7ed957", bg="black")
start_button.pack(side=tk.BOTTOM, pady=30)

title_label.pack(pady=30)
photo_label.pack(pady=30)

root.mainloop()

