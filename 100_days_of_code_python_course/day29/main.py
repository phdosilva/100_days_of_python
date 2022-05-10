from tkinter import *  # only import class and attributes
from tkinter import messagebox
import random
import pyperclip


DEFAULT_EMAIL_VALUE = "pedrohenrique@email.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# From Password Generator Project
def random_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    return "".join(password_list)


def generate_pwd():
    pwd_entry.delete(0, 'end')
    pwd = random_pwd()
    pyperclip.copy(pwd)
    pwd_entry.insert(0, pwd)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def reset_entry_fields():
    website_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    pwd_entry.delete(0, 'end')

    email_entry.insert(0, DEFAULT_EMAIL_VALUE)


def save():
    content = f'{website_entry.get()} | {email_entry.get()} | {pwd_entry.get()}\n'
    with open("pwd.txt", "a") as file:
        file.write(content)

    reset_entry_fields()


def validation():
    if website_entry.get() == "" or email_entry.get() == "" or pwd_entry.get() == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    elif messagebox.askokcancel(title=website_entry.get(),
                                message=f'These are the details entered: \n'
                                        f'Email: {email_entry.get()}'
                                        f'\nPassword: {pwd_entry.get()}'):
        save()
    else:
        reset_entry_fields()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

# Window config
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas setup
img_file = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img_file)

canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=35)
email_entry = Entry(width=35)
pwd_entry = Entry(width=21)

email_entry.insert(0, DEFAULT_EMAIL_VALUE)

website_entry.grid(row=1, column=1, columnspan=2)
email_entry.grid(row=2, column=1, columnspan=2)
pwd_entry.grid(row=3, column=1)

# Button
generate_pwd_button = Button(text="Generate Password", command=generate_pwd)
add_button = Button(text="Add", width=36, command=validation)

generate_pwd_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
