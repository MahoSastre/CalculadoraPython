import tkinter as tk
from tkinter import ttk

def click_button(value):
    current = str(entry.get())
    new_value = str(current) + str(value)
    entry.delete(0, tk.END)
    entry.insert(0, new_value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


root = tk.Tk()
root.title("Calculadora")


entry = tk.Entry(root, width=16, font=('Arial', 16), bd=10, insertwidth=4, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4, pady=10)


style = ttk.Style()
style.configure('TButton', font=('Arial', 14), padding=10)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    ttk.Button(root, text=button, command=lambda b=button: click_button(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


ttk.Button(root, text='C', command=clear_entry).grid(row=row_val, column=col_val, columnspan=2, padx=5, pady=5)


ttk.Button(root, text='=', command=calculate).grid(row=row_val, column=col_val + 2, columnspan=2, padx=5, pady=5)


root.eval('tk::PlaceWindow . center')


root.mainloop()


