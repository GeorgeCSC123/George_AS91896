import tkinter as tk

root = tk.Tk()
root.title("My App")
root.geometry("400x300")
root.configure(bg="#7ed957")

title_label = tk.Label(root, text="George’s countries quiz", fg="white", bg="#7ed957", font=("arial", 20, "bold"))

photo = tk.PhotoImage(file=r"C:\Users\relia\Downloads\12CSC\Screenshot 2026-05-19 091556.png")
photo_label = tk.Label(root, image=photo, bg="#7ed957")

photo2 = tk.PhotoImage(file=r"C:\Users\relia\Downloads\12CSC\Screenshot 2026-05-19 091833.png")
photo2_label = tk.Label(root, image=photo2, bg="#7ed957")


title_label.pack(pady=20)
photo_label.pack(pady=20)
photo2_label.pack(pady=20)

root.mainloop()
