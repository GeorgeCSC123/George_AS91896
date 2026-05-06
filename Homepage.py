import tkinter as tk


root = tk.Tk()
root.title("My App")
root.geometry("400x300")
root.configure(bg="#7ed957")
label = tk.Label(root, text="George’s countries quiz", fg="white", bg="#7ed957", font=("arial", 20, "bold"))
my_image = tk.PhotoImage(file="image1.png")
label = tk.Label(root, image=my_image)
label.pack(pady=20)


root.mainloop()

