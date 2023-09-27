import tkinter

def calculate():
    miles = float(entry_miles.get())
    kms = round(miles*1.852)
    label_answer.config(text=kms)

window = tkinter.Tk()
window.title("Mile to Km Convertor")
window.wm_minsize(width=250, height=100)
window.config(border=20)

#Labels
label_is_equal = tkinter.Label(text="is equal to")
label_is_equal.grid(column=1, row=2)
label_miles = tkinter.Label(text="Miles")
label_miles.grid(column=3, row=1)
label_km = tkinter.Label(text="Km")
label_km.grid(column=3, row=2)
label_answer = tkinter.Label(text="0")
label_answer.grid(column=2, row=2)

#Buttons
button_calculate = tkinter.Button(text="Calculate", command=calculate)
button_calculate.grid(column=2, row=3)

#Entries
entry_miles = tkinter.Entry(width=10)
entry_miles.grid(row=1, column=2)
entry_miles.config(justify="center")

window.mainloop()