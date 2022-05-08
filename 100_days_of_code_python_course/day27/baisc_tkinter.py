import tkinter

# Windows
window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)
window.config(padx=50, pady=50)

# Label
label1 = tkinter.Label(text="Hello world!", font=("Arial", 24))
label1.grid(column=0, row=0)
# label1.pack()
# label1.place(x=0, y=0)

# Button
def expose_click():
    label1.config(text=entry.get())
    print(entry.get())


button = tkinter.Button(text="Click me", command=expose_click)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="Click me", command=expose_click)
button2.grid(column=2, row=0)

# Entry
entry = tkinter.Entry(width=10)
entry.grid(column=3, row=2)

# End
window.mainloop()
