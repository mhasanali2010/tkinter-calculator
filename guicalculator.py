import tkinter as tk
from tkinter import ttk

def on_click(value):
    text.configure(state="normal")
    current = text.get()

    if value == "=":
        try:
            expression = current.replace("x", "*").replace("÷", "/").replace("^2", "**2")
            result = str(eval(expression))
            text.delete(0, tk.END)
            text.insert(0, result)
        except Exception:
            text.delete(0, tk.END)
            text.insert(0, "ERROR")
    elif value == "C":
        text.delete(0, tk.END)
    else:
        text.insert(tk.END, value)
    
    text.configure(state="readonly")

root = tk.Tk()
root.geometry("400x600")
root.title("GUI Calculator")

for i in range(5):
    root.grid_rowconfigure(i, weight = 1)
for j in range(4):
    root.grid_columnconfigure(j, weight = 1)


text = ttk.Entry(root, font=("Arial", 20))
text.grid(row=0, column=0, columnspan=3,  sticky="nsew")
text.configure(state="readonly")

buttons = [
                                           ("C", 0, 3),
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("x", 3, 3),
    ("0", 4, 0), ("^2", 4, 1), ("=", 4, 2), ("÷", 4, 3)
]

for (text_val, rowN, colN) in buttons:
    btn = ttk.Button(root, text = text_val, command=lambda val = text_val: on_click(val))
    btn.grid(row=rowN, column=colN, sticky="nsew")


root.mainloop()