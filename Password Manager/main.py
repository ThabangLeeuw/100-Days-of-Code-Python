from tkinter import *
from tkinter import messagebox
import string
import random
import pandas as pd
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    alphnum = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
    password = ""
    alph_count = 0
    num_count = 0
    punc_count = 0
    for i in range(12):
        if random.choice(alphnum).isalpha() and alph_count <= 8:
            password += random.choice(alphnum)
            alph_count += 1
        elif random.choice(alphnum).isdigit() and num_count <= 2:
            password += random.choice(alphnum)
            num_count += 1
        else:
            password += random.choice(alphnum)
            punc_count += 1

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    password_data = {"Website": [website_input.get()], "Email/Username": [email_input.get()], "Password":[password_input.get()]}

    for index, value in password_data.items():
        if "".join(value) == "":
            messagebox.showerror("Error", f"{index} cannot be empty")
            return
    df = pd.DataFrame(password_data)
    df = df.to_csv("password.csv", mode= "a", index=False, header=False,)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white", highlightthickness=0)

canvas = Canvas(width=200, height=200, bg="white")
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_name_label = Label(text= "Website: ", bg="white")
website_name_label.grid(row=1, column=0)

website_input = Entry()
website_input.config(bg="white", width=35)
website_input.grid(row=1, column=1)

email_label = Label(text= "Email/Username: ", bg="white")
email_label.grid(row=2, column=0)
email_input = Entry()
email_input.config(bg="white", width=35)
email_input.grid(row=2, column=1)

password_label = Label(text= "Password: ", bg="white")
password_label.grid(row=3, column=0)
password_input = Entry(width=21)
password_input.config(bg="white")
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", bg="white", fg="black", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", bg="white", fg="black", command=save_password)
add_button.grid(row=4, column=1)




window.mainloop()