import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk


def show_x():
    value = x_entry.get()
    result_label.config(text=f"This is x: {value}")


root = tk.Tk()
root.title("Enter x")
root.state("zoomed")
root.minsize(480, 320)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

content = ttk.Frame(root)
content.grid(row=0, column=0)

heading_font = tkfont.Font(root=root, size=18)
input_font = tkfont.Font(root=root, size=16)
button_font = tkfont.Font(root=root, size=14)
button_style = ttk.Style(root)
button_style.configure("Responsive.TButton", font=button_font)

prompt_label = ttk.Label(content, text="Enter a value for x:", font=heading_font)
prompt_label.pack(pady=(0, 8))

x_entry = ttk.Entry(content, font=input_font, justify="center")
x_entry.pack(fill="x")

show_button = ttk.Button(content, text="Show x", command=show_x, style="Responsive.TButton")
show_button.pack(pady=10)

result_label = ttk.Label(content, text="", font=heading_font)
result_label.pack()


def resize_gui(event):
    if event.widget is not root:
        return

    scale = min(event.width / 900, event.height / 600)
    scale = max(0.75, min(scale, 2.0))

    heading_font.configure(size=max(12, round(18 * scale)))
    input_font.configure(size=max(12, round(16 * scale)))
    button_font.configure(size=max(12, round(14 * scale)))
    x_entry.configure(width=max(20, round(32 * scale)))
    content.configure(padding=max(12, round(24 * scale)))
    prompt_label.pack_configure(pady=(0, max(4, round(8 * scale))))
    show_button.pack_configure(pady=max(6, round(10 * scale)))
    show_button.configure(
        padding=(max(8, round(14 * scale)), max(4, round(7 * scale))),
        width=max(12, round(16 * scale)),
    )


root.bind("<Configure>", resize_gui)

root.mainloop()