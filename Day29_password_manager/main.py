from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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
    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as f:
            # Reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            # Updating old data with new data
            data.update(f)
            with open("data.json", "w") as f:
            # Saving updated data
                json.dump(data, f, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- RESET ENTRY FIELDS ------------------------------- #
def reset_fields():
    website = entry_website.delete(0, END)
    password = entry_password.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = entry_website.get()
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


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

entry_website = Entry(width=21)
entry_website.focus()
entry_website.grid(column=1, row=1)

button_search = Button(text="Search", width=13, command=find_password)
button_search.grid(row=1, column=2)


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
