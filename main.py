from tkinter import *
from tkinter import messagebox
import random

FONT_TUPLE = ("Arial", 17, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [random.choice(letters) for _ in range(4)]
    pw_symbols = [random.choice(symbols) for _ in range(2)]
    pw_numbers = [random.choice(numbers) for _ in range(2)]

    password_list = pw_letters + pw_symbols + pw_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user = user_entry.get()
    pw = pw_entry.get()

    if len(website) == 0 or len(user) == 0 or len(pw) == 0:
        messagebox.showerror(title="Error", message="Please fill all fields.")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                              "\n\n"
                                                              f"Email: {user}"
                                                              f"\nPassword: {pw}"
                                                              "\n\n"
                                                              "Is it ok to save?")
        if is_ok:
            data_line = f"{website} | {user} | {pw}"
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

gen_pw_button = Button(text="Generate Password", command=generate_password)
gen_pw_button.grid(column=2, row=3)

add_pw_button = Button(text="Add", width=36, command=save)
add_pw_button.grid(column=0, row=4, columnspan=3)

window.mainloop()
