import tkinter as tk


# function print name
def submit_name():
   print(f"Name entered: {name_entry.get()}")


# function clear window
def clear_window():
   for widget in root.winfo_children():
       widget.destroy()


# function questions page
def questions_page():
   clear_window()


# main window
root = tk.Tk()
root.title("My App")
root.geometry("900x700")
root.configure(bg="#7ed957")


# title
title_label = tk.Label(root, text="George’s countries quiz", fg="white", bg="#7ed957", font=("arial", 40, "bold"))


# image and displaying
photo = tk.PhotoImage(file=r"C:\Users\23068\OneDrive - Mt Roskill Grammar School\Documents\Vscode y12\photo1.png")
photo_label = tk.Label(root, image=photo, bg="#7ed957")


# start button image
photo2 = tk.PhotoImage(file=r"C:\Users\23068\OneDrive - Mt Roskill Grammar School\Documents\Vscode y12\photo2.png")


# image button
start_button = tk.Button(root, image=photo2, command=questions_page, bd=0, relief="flat", highlightthickness=0, bg="#7ed957",
                        activebackground="#7ed957", cursor="hand2")


# frame
user_frame = tk.Frame(root,bg="white",padx=20,pady=10)


# name entry text
name_label = tk.Label(user_frame, text="Enter name to start", font=("Arial", 16, "bold"), bg="white", fg="black")


#  name entry box
name_entry = tk.Entry(user_frame, font=("Arial", 20), bg="white", fg="black", bd=2, relief="solid", justify="center")


# submit button
submit_button = tk.Button(user_frame, text="Submit Name", command=submit_name, font=("Arial", 20, "bold"), fg="#7ed957", bg="black",
                         activebackground="gray20", activeforeground="white", cursor="hand2")


# positioning of widgets
title_label.pack(pady=5)
photo_label.pack(pady=5)
start_button.pack(pady=5)
user_frame.pack(pady=5)
name_label.pack(pady=5)
name_entry.pack(pady=5, ipady=5)
submit_button.pack(pady=5)


# keeps window running
root.mainloop()
