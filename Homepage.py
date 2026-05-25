import tkinter as tk

def submit_name():
    print(f"Name entered: {name_entry.get()}")

# main window sizing and bg colour
root = tk.Tk()
root.title("My App")
root.geometry("800x600")
root.configure(bg="#7ed957")

# creating title
title_label = tk.Label(root, text="George’s countries quiz", fg="white", bg="#7ed957", font=("arial", 40, "bold"))

# creating image and displaying
photo = tk.PhotoImage(file=r"C:\Users\23068\OneDrive - Mt Roskill Grammar School\Documents\Screenshot 2026-05-19 091556.png")
photo_label = tk.Label(root, image=photo, bg="#7ed957")

# creating start quiz button
start_button = tk.Button(root, text="Start Quiz", font=("Arial", 40, "bold"), fg="#7ed957", bg="black")

# creating the name entry box
name_entry = tk.Entry(root, font=("Arial", 40), bg="white", fg="black", bd=2, relief="solid", justify="center")

# creating a submit button for the name
submit_button = tk.Button(root, text="Submit Name", command=submit_name, font=("Arial", 25, "bold"), fg="white", bg="black")

# positioning of widgets
title_label.pack(pady=10)
photo_label.pack(pady=10)
start_button.pack(pady=10)
name_entry.pack(pady=10, ipady=5)
submit_button.pack(pady=10)

# keeps window running
root.mainloop()

