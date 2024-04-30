from tkinter import *
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x500+300+200")
root.resizable(False, False)

root.configure(bg="#f0f1f5")


def calculate_bmi():
    h = int(Height.get())
    w = int(Weight.get())
    print(f"{type(h)} x {type(w)}")


#Bottom
Label(root, width=70, height=18, bg="#434544").pack(side="bottom")


# Entry Box
Height = IntVar()
Weight = IntVar()

Label(root, text="Height: (m)", font='arial 18').place(x=30, y=90)
Height = Entry(root, textvariable=Height, width=6, font='arial 30', bg="#c2c2c2", fg="#000", bd=0, justify=CENTER)
Height.place(x=30, y=120)
Height.focus()

Label(root, text="Weight: (kg)", font='arial 18').place(x=230, y=90)
Weight = Entry(root, textvariable=Weight, width=6, font='arial 30', bg="#c2c2c2", fg="#000", bd=0, justify=CENTER)
Weight.place(x=230, y=120)
Weight.focus()

s = ttk.Style()
s.configure('my.TButton', font=('Arial', 18))
btn_calculate = ttk.Button(root, text="Calculate", style='my.TButton', command=calculate_bmi).place(x=120, y=180)

root.mainloop()