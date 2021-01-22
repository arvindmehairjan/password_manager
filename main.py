from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = enter_field_website.get()
    email = enter_field_email.get()
    password = enter_password.get()

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
enter_password = Entry(width=21)
enter_password.grid(column=1, row=3)

generate_password = Button(text="Generate Password")
generate_password.grid(column=2, row=3)

submit_button = Button(text="Add", width=36, command=save)
submit_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
