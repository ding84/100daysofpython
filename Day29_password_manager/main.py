from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    if len(entry_password.get()) != 0:
        entry_password.delete(0, END)

    nr_letters = [choice(letters) for _ in range(randint(8, 10))]
    nr_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    nr_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = nr_letters + nr_symbols + nr_numbers
    shuffle(password_list)
    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = entry_website.get()
    username = entry_mailuser.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nUsername: {username} \n "
                                                      f"Password: {password}\n Is that correct?")
        if is_ok:
            with open("passwords.txt", "a") as f:
                f.write(f"{website} | {username} | {password}\n")
                entry_website.delete(0, END)
                entry_password.delete(0, END)


def reset_fields():
    website = entry_website.delete(0, END)
    password = entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#ffffff")

bg_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="#ffffff")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(column=1, row=0)

label_website = Label(text="Website: ", bg="#ffffff")
label_website.grid(column=0, row=1)

entry_website = Entry(width=35)
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2)

label_mailuser = Label(text="Email/Username: ", bg="#ffffff")
label_mailuser.grid(column=0, row=2)

entry_mailuser = Entry(width=35)
entry_mailuser.insert(0, "dirk@mail.me")
entry_mailuser.grid(column=1, row=2, columnspan=2)

label_password = Label(text="Password: ", bg="#ffffff")
label_password.grid(column=0, row=3)

entry_password = Entry(width=21)
entry_password.grid(column=1, row=3)

button_password = Button(text="Generate Password", width=16, font=("Arial", 10, "normal"), padx=0, pady=0,
                         bg="#ffffff", command=generate_password)
button_password.grid(column=2, row=3)

button_add = Button(text="Add", bg="#ffffff", width=10, command=save_data)
button_add.grid(column=1, row=4)

button_reset = Button(text="Reset", bg="#ffffff", width=10, command=reset_fields)
button_reset.grid(column=2, row=4)
window.mainloop()
