from tkinter import *

window = Tk()
window.config(width=300, height=200, padx=10, pady=10)
window.title("Mile to KM Converter")


def calculate():
    km_label["text"] = round(float(user_input.get()) * 1.609, 2)


user_input = Entry(width=10)
user_input.grid(column=1, row=0, padx=5, pady=5)

my_label = Label(text="Miles")
my_label.grid(column=2, row=0, padx=5, pady=5)

equal_label = Label(text="is equal to ", padx=5, pady=5)
equal_label.grid(column=0, row=1)

km_label = Label(text="0")
km_label.grid(column=1, row=1)

output_label = Label(text="KM")
output_label.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=3)



window.mainloop()
