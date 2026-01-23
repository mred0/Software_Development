import tkinter as tk

def show_message():
    name = name_entry.get()
    if name:
        result_label.config(text=f"Hello, {name}! Welcome to the app.")
    else:
        result_label.config(text="Please enter your name.")

window = tk.Tk()
window.title("Simple GUI Application")
window.geometry("300x200")

title_label = tk.Label(window, text="Greeting App", font=("Arial", 14))
title_label.pack(pady=10)

name_label = tk.Label(window, text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack(pady=5)

submit_button = tk.Button(window, text="Submit", command=show_message)
submit_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
