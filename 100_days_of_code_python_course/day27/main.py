import tkinter

window = tkinter.Tk()


window.title("My first GUI program")
window.minsize(width=500,height=300)

label1 = tkinter.Label(text="Hello world!", font=("Arial", 24))
label1.pack()


def expose_click():
    label1.config(text=input.get())
    print(input.get())


button = tkinter.Button(text="Click me", command=expose_click)
button.pack()

input = tkinter.Entry(width=10)
input.pack()

window.mainloop()
