from tkinter import *

window = Tk()
window.config(padx=20, pady=20)

# Entry
entry = Entry(width=10)
entry.grid(column=1, row=0)

# Labels
label1 = Label(text="Is equal to")
label1.grid(column=0, row=1)

label2 = Label(text="0")
label2.grid(column=1, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

# Button
def calculate_result():
    result = float(entry.get()) * 1.689
    label2.config(text=result)


button = Button(text="Calculate", command=calculate_result)
button.grid(column=1, row=2)


window.mainloop()