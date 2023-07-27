from tkinter import *
from tkinter import messagebox
from random import choice, shuffle
import json
from PIL import Image, ImageTk
# generate
from typing import List, Union, Any

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "A", "B", "C", "D", "E",
           "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "~"]
random_list = []


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    global random_list
    random_list.clear()
    random_l = [choice(letters) for j in range(8)]
    random_n = [choice(numbers) for i in range(2)]
    random_s = [choice(symbols) for i in range(2)]
    random_list = random_l + random_n + random_s
    shuffle(random_list)
    generated_pass = "".join(random_list)
    pass_ent.delete(0, END)
    pass_ent.insert(0, generated_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    web = web_ent.get()
    em = email_ent.get()
    pas = pass_ent.get()
    new_data = {web: {"email": em, "password": pas, }}
    if web == "" or pas == "":
        messagebox.showerror(title="ERROR", message="Please Fill All Details!!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating the data
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        # with open("data.txt", "a") as data:
        #     data.write(f"{web} | {em} | {pas}\n")
        #     web_ent.delete(0, END)
        #     pass_ent.delete(0, END)
        ####----With json library
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=2)
            web_ent.delete(0, END)
            pass_ent.delete(0, END)

#-------------------------------Find Password-------------------------#
def find_password():
    website_entry = web_ent.get()
    with open("data.json") as data_file:
        try:
            data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="error", message="Data NOT FOUND")
        else:
            if website_entry in data:
                email_access = data[website_entry]["email"]
                password_access = data[website_entry]["password"]
                messagebox.showinfo(title=website_entry, message=f"Email:- {email_access}\nPassword:- {password_access}")
            else:
                messagebox.showinfo(title="Not Found", message="The website that you are looking for is not saved!!")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=100, pady=70)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
# logo_img=Image.open("password-manager-start\logo.png")
# logo_img=ImageTk.PhotoImage(logo_img)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
# Labels
website = Label(text="Website:")
website.grid(row=1, column=0)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# entry
web_ent = Entry(width=32)
web_ent.grid(row=1, column=1)
web_ent.focus()

email_ent = Entry(width=50)
email_ent.grid(row=2, column=1, columnspan=2)
email_ent.insert(0, "@gmail.com")

pass_ent = Entry(width=32)
pass_ent.grid(row=3, column=1)
# buttons
search = Button(text="Search", width=14, command=find_password)
search.grid(row=1, column=2)

generate_pass = Button(text="Generate Password", command=generate)
generate_pass.grid(row=3, column=2)

add = Button(text="Add", width=43, command=add)
add.grid(row=4, column=1, columnspan=2)
window.mainloop()
