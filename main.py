from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
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

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please enter your information!")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \n "
                                                                f"Email: {email} \n Password: {password} \nAre these information correct?")

        if is_okay:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                enter_field_website.delete(0, END)
                enter_password.delete(0, END)


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

enter_field_website = Entry(width=35)
enter_field_website.grid(column=1, row=1, columnspan=2)
enter_field_website.focus()
enter_field_email = Entry(width=35)
enter_field_email.grid(column=1, row=2, columnspan=2)
enter_field_email.insert(END, "example@email.com")
enter_password = Entry(width=21, text=gen_pass)
enter_password.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=gen_pass)
generate_password.grid(column=2, row=3)

submit_button = Button(text="Add", width=36, command=save)
submit_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
