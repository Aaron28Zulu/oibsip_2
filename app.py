from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



# Global variables
universal_font_header = ('Arial', 30,)
universal_font_other = ('Arial', 12)
universal_font_combobox = ('Arial', 18,)


root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x600")
root.resizable(False, False)

root.configure(bg="#f0f1f5")

def calculate_bmi():
    """
    Height value & Weight value and Calculate
    """
    try:
        weight = float(Weight.get())
        height = float(Height.get())
        
        bmi = weight / (height**2)

        # print(f"{height} and {weight} type: {type(height)} and {type(weight)} respectively")
        result_label.configure(text="Your BMI is: {:.1f}".format(bmi))

    except ValueError:
        messagebox.showerror('error', 'Enter a valid number')

    except ZeroDivisionError:
        messagebox.showerror('error', 'Can not divide with 0!')


style = ttk.Style()
style.configure('BMI.TLabel', font=universal_font_header)
title = ttk.Label(root, text="Calculate BMI", style='BMI.TLabel')
title.place(relx=0.17, rely=0.02)


# Entry Box
Height = StringVar()
Weight = StringVar()


ttk.Label(root, text="Enter Height in m: ").place(relx=0.19, rely=0.13)
height_entry = ttk.Entry(root, width=10, textvariable=Height, justify=CENTER, font=universal_font_other)
height_entry.focus()
height_entry.place(relx=0.54, rely=0.13)


ttk.Label(root, text="Enter weight in kg: ").place(relx=0.19, rely=0.19)
weight_entry = ttk.Entry(root, width=10, textvariable=Weight, justify=CENTER, font=universal_font_other)
weight_entry.focus()
weight_entry.place(relx=0.54, rely=0.19)


s = ttk.Style()
s.configure('my.TButton', font=('Arial', 12), background='#fff')
btn_calculate = ttk.Button(root, text="Calculate", style='my.TButton', command=calculate_bmi, cursor='hand2')
btn_calculate.place(relx=0.33, rely=0.28)

result_label = ttk.Label(root, text=' ', font=universal_font_other, width=25, background="#fff", foreground="#000")
result_label.config(anchor='center')
result_label.place(relx=.19, rely=.38)

root.mainloop()