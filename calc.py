from tkinter import *
import tkmacosx as tk


def add_digit(digit):
    value = calc.get()
    if value[0] == "0" and len(value) == 1:
        value = value[1:]
    calc.delete(0, END)
    calc.insert(0, value+str(digit))


def add_operation(operation):
    value = calc.get()
    if value[-1] in "-+/*":
        value = value[:-1]
    calc.delete(0, END)
    calc.insert(0, value+operation)


def calculate():
    value = calc.get()
    if value[-1] in "-=*/":
        value = value + value[:-1]
    calc.delete(0, END)
    calc.insert(0, eval(value))


def del_all():
    calc.delete(0, END)
    calc.insert(0, "0")


def del_last():
    value = calc.get()

    if len(value) != 1 and value != 0:
        value = value[:-1]
    elif len(value) == 1:
        value = "0"
    calc.delete(0, END)
    calc.insert(0, value)


def bracket():
    value = calc.get()
    if value[0] == "0":
        value = value[1:]
        value = value + "("
    elif value[-1] in "0123456789":
        value = value + ")"
    else:
        value = value + "("
    calc.delete(0, END)
    calc.insert(0, value)


def point():
    value = calc.get()
    if value[-1] in "0123456789":
        value = value + "."
    calc.delete(0, END)
    calc.insert(0, value)


def change():
    value = calc.get()
    if value[0] == "-":
        value = value[1:]
    else:
        value = "-" + value
    calc.delete(0, END)
    calc.insert(0, value)


def make_button_dig(digit):
    return tk.Button(text=f"{digit}", bd=4, command=lambda: add_digit(digit))


def make_button_op(operation):
    return tk.Button(text=f"{operation}", bd=4, command=lambda: add_operation(operation))


def make_button_eq(operation):
    return tk.Button(text=f"{operation}", bd=4, command=calculate)


win = Tk()
win.title("Калькулятор")
win.geometry("442x247")
win.config(bg="black")


calc = Entry(win, justify="right", font="arial 25", bd=4)
calc.insert(0, "0")
calc.grid(row=0, column=0, columnspan=3, stick="we")


i = 1
for row in range(3):
    for column in range(3):
        make_button_dig(i).grid(row=row+2, column=column, sticky="wens", padx=3, pady=3)
        i += 1


tk.Button(win, text="⌫", bd=4, command=del_last).grid(row=0, column=3, padx=3, pady=3)
tk.Button(win, text="C", bd=4, command=del_all).grid(row=1, column=0, padx=3, pady=3)
tk.Button(win, text="()", bd=4, command=bracket).grid(row=1, column=1, padx=3, pady=3)
tk.Button(win, text="%", bd=4).grid(row=1, column=2, padx=3, pady=3)
make_button_op("/").grid(row=1, column=3, padx=3, pady=3)
make_button_op("*").grid(row=2, column=3, padx=3, pady=3)
make_button_op("-").grid(row=3, column=3, padx=3, pady=3)
make_button_op("+").grid(row=4, column=3, padx=3, pady=3)
tk.Button(win, text="±", bd=4, command=change).grid(row=5, column=0, padx=3, pady=3)
make_button_dig("0").grid(row=5, column=1, padx=3, pady=3)
tk.Button(win, text=".", bd=4, command=point).grid(row=5, column=2, padx=3, pady=3)
make_button_eq("=").grid(row=5, column=3, padx=3, pady=3)


win.mainloop()
