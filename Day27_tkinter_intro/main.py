from tkinter import *

window = Tk()
window.title("Tkinter window")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
# label
my_label = Label(text="Label goes here", font=("Arial", 12, "bold"))
my_label.grid(row=0, column=0)
my_label.config(padx=20, pady=20)
# my_label["text"] = "My text"
# my_label.config(text="New text")


def button_clicked():
    user_input = input.get()
    my_label.config(text=user_input)


button = Button(text="Click me", command=button_clicked)
button.grid(column=0, row=3)

new_button = Button(text="Click me too")
new_button.grid(column=2, row=1)

# entry component

input = Entry(width=10)
input.grid(column=3, row=3)

#
# layout managers
#

# place uses coordinates (x, y)

# grid uses table like positioning


# has to be at the end of the program
window.mainloop()
