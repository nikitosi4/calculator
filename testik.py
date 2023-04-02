from tkinter import *
import tkmacosx as tk


def add_digit(digit):
    value = calc.get()
    if value[0] == "0":
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


def make_button_dig(digit):
    return tk.Button(text=f"{digit}", bd=4, command=lambda: add_digit(digit))


def make_button_op(operation):
    return tk.Button(text=f"{operation}", bd=4, command=lambda: add_operation(operation))


def make_button_eq(operation):
    return tk.Button(text=f"{operation}", bd=4, command=calculate)


win = Tk()
win.title("Калькулятор")
win.geometry("456x220")
win.config(bg="black")


calc = Entry(win, justify="right", font="arial 25")
calc.insert(0, "0")
calc.grid(row=0, column=0, columnspan=3, stick="we", padx=5)


i = 1
for row in range(3):
    for column in range(3):
        make_button_dig(i).grid(row=row+1, column=column, sticky="wens", padx=5, pady=5)
        i += 1

make_button_dig("0").grid(row=4, column=0, sticky="wens", padx=5, pady=5)
make_button_op("+").grid(row=1, column=3, sticky="wens", padx=5, pady=5)
make_button_op("-").grid(row=2, column=3, sticky="wens", padx=5, pady=5)
make_button_op("*").grid(row=3, column=3, sticky="wens", padx=5, pady=5)
make_button_op("/").grid(row=4, column=3, sticky="wens", padx=5, pady=5)
make_button_eq("=").grid(row=4, column=2, sticky="wens", padx=5, pady=5)
tk.Button(win, text=("C"), bd=4, command=del_all).grid(row=4, column=1)
tk.Button(win, text=("⌫"), bd=4, command=del_last).grid(row=0, column=3)

win.mainloop()
