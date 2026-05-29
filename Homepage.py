import tkinter as tk

#print functions
def submit_name():
    print(f"Name entered: {name_entry.get()}")

def start_quiz():
    print("Quiz started!")

# clear text
def clear(event):
    if name_entry.get() == "Enter name to start":
        name_entry.delete(0, tk.END)


# main window
root = tk.Tk()
root.title("My App")
root.geometry("950x700")
root.configure(bg="#7ed957")

# title
title_label = tk.Label(root, text="George’s countries quiz", fg="white", bg="#7ed957", font=("arial", 50, "bold"))

# image and displaying
photo = tk.PhotoImage(file=r"C:\Users\23068\OneDrive - Mt Roskill Grammar School\Documents\Vscode y12\Screenshot 2026-05-19 091556.png")
photo_label = tk.Label(root, image=photo, bg="#7ed957")

# start button image
photo2 = tk.PhotoImage(file=r"C:\Users\23068\OneDrive - Mt Roskill Grammar School\Documents\Vscode y12\Screenshot 2026-05-27 142520.png")

# image button
start_button = tk.Button(root, image=photo2, command=start_quiz, bd=0, relief="flat", highlightthickness=0, bg="#7ed957",
                         activebackground="#7ed957", cursor="hand2")

#  name entry box
name_entry = tk.Entry(root, font=("Arial", 35), bg="white", fg="black", bd=2, relief="solid", justify="center")

# enter name text
name_entry.insert(0, "Enter name to start")

# clears the text
name_entry.bind("<FocusIn>", clear)

# submit button
submit_button = tk.Button(root, text="Submit Name", command=submit_name, font=("Arial", 30, "bold"), fg="white", bg="black",
                          activebackground="gray20", activeforeground="white", cursor="hand2")

# positioning of widgets
title_label.pack(pady=10)
photo_label.pack(pady=10)
start_button.pack(pady=10)
name_entry.pack(pady=10, ipady=5)
submit_button.pack(pady=10)

# keeps window running
root.mainloop()
