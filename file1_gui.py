import tkinter as tk
from tkinter import ttk


def show_x():
    value = x_entry.get()
    result_label.config(text=f"This is x: {value}")


root = tk.Tk()
root.title("Enter x")
root.geometry("300x150")

ttk.Label(root, text="Enter a value for x:").pack(pady=(16, 4))

x_entry = ttk.Entry(root)
x_entry.pack()

ttk.Button(root, text="Show x", command=show_x).pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()