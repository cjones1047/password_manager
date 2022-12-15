from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_TUPLE = ("Arial", 17, "normal")


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    searched_website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",
                            message="No websites have been added yet.")
    else:
        if searched_website in data:
            email = data[searched_website]["email"]
            password = data[searched_website]["password"]
            messagebox.showinfo(title=searched_website,
                                message=f"Username: {email}\n"
                                        f"Password: {password}")
        else:
            messagebox.showinfo(title="Sorry",
                                message="That website hasn't been added yet. Please check spelling "
                                        "and capitalization.")


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

    pw_entry.delete(0, END)
    pw_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Password Copied", message="Generated password was automatically copied to clipboard.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user = user_entry.get()
    pw = pw_entry.get()
    new_data = {
        website: {
            "email": user,
            "password": pw,
        }
    }

    if len(website) == 0 or len(user) == 0 or len(pw) == 0:
        messagebox.showerror(title="Error", message="Please fill all fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
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

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky='W')

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="nsew")

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
gen_pw_button.grid(column=2, row=3, sticky="nsew")

add_pw_button = Button(text="Add", width=36, command=save)
add_pw_button.grid(column=0, row=4, columnspan=3)

window.mainloop()
