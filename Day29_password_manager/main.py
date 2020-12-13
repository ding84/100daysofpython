from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = entry_website.get()
    username = entry_mailuser.get()
    password = entry_password.get()
    with open("passwords.txt", "a") as f:
        f.write(f"{website} | {username} | {password}\n")
    entry_website.delete(0, END)
    entry_password.delete(0, END)


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

button_password = Button(text="Generate Password", width=16, font=("Arial", 10, "normal"), padx=0, pady=0, bg="#ffffff")
button_password.grid(column=2, row=3)

button_add = Button(text="Add", width=33, bg="#ffffff", command=save_data)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()
