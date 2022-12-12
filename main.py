from tkinter import *

FONT_TUPLE = ("Arial", 17, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    data_line = f"{website_entry.get()} | {user_entry.get()} | {pw_entry.get()}"
    with open("data.txt", "a") as data:
        data.write(f"{data_line}\n")
    # clear entry fields except user_entry
    website_entry.delete(0, END)
    pw_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky='E')

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky='W')

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2, sticky='E')

user_entry = Entry(width=35)
user_entry.insert(0, "default@email.com")
user_entry.grid(column=1, row=2, columnspan=2, sticky='W')

pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3, sticky='E')

pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3, sticky='W')

gen_pw_button = Button(text="Generate Password")
gen_pw_button.grid(column=2, row=3)

add_pw_button = Button(text="Add", width=36, command=save)
add_pw_button.grid(column=0, row=4, columnspan=3)

window.mainloop()
