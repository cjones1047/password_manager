from tkinter import *

FONT_TUPLE = ("Arial", 17, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
padlock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text="Website:", font=FONT_TUPLE)
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

user_label = Label(text="Email/Username:", font=FONT_TUPLE)
user_label.grid(column=0, row=2)

user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)

pw_label = Label(text="Password:", font=FONT_TUPLE)
pw_label.grid(column=0, row=3)

pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3)

gen_pw_button = Button(text="Generate Password")
gen_pw_button.grid(column=2, row=3)

add_pw_button = Button(text="Add", width=36)
add_pw_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
