import random
import string
import customtkinter as CTk

def generate_password():
    password = ''
    if var_numbers.get():
        password += ''.join(random.sample(string.digits, min(len(string.digits), 16 - len(password))))
    if var_lowercase.get():
        password += ''.join(random.sample(string.ascii_lowercase, min(len(string.ascii_lowercase), 16 - len(password))))
    if var_uppercase.get():
        password += ''.join(random.sample(string.ascii_uppercase, min(len(string.ascii_uppercase), 16 - len(password))))
    if var_special.get():
        password += ''.join(random.sample(string.punctuation, min(len(string.punctuation), 16 - len(password))))

    password_entry.delete(0, CTk.END)
    password_entry.insert(0, password)

root = CTk.CTk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width//3}x{screen_height//3}")
root.title("PassGEN BY ARGENT")

var_numbers = CTk.IntVar()
numbers_check = CTk.CTkCheckBox(root, text="0-9", variable=var_numbers, font=("Helvetica", int(screen_height//30)))
var_lowercase = CTk.IntVar()
lowercase_check = CTk.CTkCheckBox(root, text="a-z", variable=var_lowercase, font=("Helvetica", int(screen_height//30)))
var_uppercase = CTk.IntVar()
uppercase_check = CTk.CTkCheckBox(root, text="A-Z", variable=var_uppercase, font=("Helvetica", int(screen_height//30)))
var_special = CTk.IntVar()
special_check = CTk.CTkCheckBox(root, text="@#$%", variable=var_special, font=("Helvetica", int(screen_height//30)))

password_entry = CTk.CTkEntry(root, font=("Helvetica", int(screen_height//30)))
generate_button = CTk.CTkButton(root, text="Generate", command=generate_password, font=("Helvetica", int(screen_height//15)))

numbers_check.pack(pady=int(screen_height//100))
lowercase_check.pack(pady=int(screen_height//100))
uppercase_check.pack(pady=int(screen_height//100))
special_check.pack(pady=int(screen_height//100))
password_entry.pack(pady=int(screen_height//100))
generate_button.pack(pady=int(screen_height//100))

root.pack_propagate(0)

root.mainloop()