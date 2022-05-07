# import tkinter
#
# window = tkinter.Tk()
#
#
# window.title("My first GUI program")
# window.minsize(width=500,height=300)
#
# tkinter.Label(text="Hello world!", font=("Arial", 24)).pack()
# 2
# window.mainloop()


# unlimited arguments

# def add(*args):
#     if len(args) <= 1:
#         return args[0]
#
#     return add(*args[1:]) + args[0]
#
# print(add(1,2,3,4,5))


# kwargs arguments

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.number_of_seats = kw.get("number_of_seats")


my_car = Car(make="Nissan")
print(my_car.make)

