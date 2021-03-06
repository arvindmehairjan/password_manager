from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password_generated = "".join(password_list)
    enter_password.insert(0, password_generated)
    pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = enter_field_website.get()
    email = enter_field_email.get()
    password = enter_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please enter your information!")
    else:
        try:
            with open("data.json", "r") as data_file:

                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        except FileNotFoundError:
            with open("data.json", "a") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            enter_field_website.delete(0, END)
            enter_password.delete(0, END)


# ---------------------------- FIND PASSWORD -------------------------- #
def find_password():
    website = enter_field_website.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

enter_field_website = Entry(width=21)
enter_field_website.grid(column=1, row=1)
enter_field_website.focus()
enter_field_email = Entry(width=35)
enter_field_email.grid(column=1, row=2, columnspan=2)
enter_field_email.insert(END, "example@email.com")
enter_password = Entry(width=21, show='*')
enter_password.grid(column=1, row=3)

search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(column=2, row=1)
generate_password = Button(text="Generate Password", command=gen_pass)
generate_password.grid(column=2, row=3)

submit_button = Button(text="Add", width=36, command=save)
submit_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
