from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    final_password = "".join(password_list)

    password_entry.insert(0, final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def is_empty():
    messagebox.showerror(title="Error", message="Please don't leave any fields empty!")


def clicked():
    my_website = website_entry.get()
    my_email = email_entry.get()
    my_password = password_entry.get()
    if len(my_website) == 0 or len(my_password) == 0 or len(my_email) == 0:
        is_empty()
    else:
        messagebox.askokcancel(title=f"{my_website}",
                               message=f"Here's the information you entered:\n {my_website} , {my_email} , {my_password}"
                                       f"\n Is it okay to save?")
        data = open("data.txt", "a")
        data.write(f"({my_website} , {my_email} , {my_password})\n")
        data.close()
        website_entry.delete(0, END)
        email_entry.delete(0,END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(padx=30, pady=30)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

password_entry = Entry(width=52)
password_entry.grid(column=1, row=3, columnspan=2)

generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3)

add = Button(text="Add", width=44, command=clicked)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()

