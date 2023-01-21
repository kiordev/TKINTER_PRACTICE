import tkinter
import tkinter as tk
from tkinter import LEFT, W
import customtkinter

#DATA_BASE
data_base_login = "sasha"
data_base_password = "12345"
def check_the_data():
    global data_base_password
    global data_base_login
    global message
    if login_entry_field.get() == data_base_login and password_entry_field.get() == data_base_password:
        message = tk.Label(root, text="ВХОД!",
                 bg="#3C143C",
                 fg="green",
                 font=('Arial', 12, 'bold'))
        message.grid(row=4, column=0, sticky=W, padx=10)
        message.after(3000, message.destroy)
    else:
        message = tk.Label(root, text="""ЛОЖНЫЕ ДАННЫЕ""",
                 bg="#3C143C",
                 fg="red",
                 font=('Arial', 12, 'bold'),
                 justify=LEFT)
        message.grid(row=4, column=0, sticky=W, padx=10)
        message.after(3000, message.destroy)

# Main Window Settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk(fg_color="#3C143C")
root.geometry("600x600")
root.resizable(False, False)
root.title("Custom Entry Test")

# Autorization LABEL
main_label = tk.Label(root,
                      text="AUTORIZATION",
                      bg="#3C143C",
                      fg="white",
                      font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky=W, padx=10)
# Name_Label
login_label = tk.Label(root,
                      text="LOGIN",
                      bg="#3C143C",
                      fg="white",
                      anchor="w",
                      justify=LEFT,
                      font=('Arial', 12, 'bold')).grid(row=1, column=0, columnspan=1, sticky=W, padx=10, pady=10)
# Password_Label
password_label = tk.Label(root,
                      text="PASSWORD",
                      bg="#3C143C",
                      fg="white",
                      font=('Arial', 12, 'bold')).grid(row=2, column=0, sticky=W, padx=10, pady=10)
# Login Entry
login_entry_field = customtkinter.CTkEntry(master=root,
                                           fg_color="#270A41")
# Password Entry
password_entry_field = customtkinter.CTkEntry(master=root,
                                              fg_color="#270A41")

button_submit = customtkinter.CTkButton(root,text="SUBMIT",
                                        command=check_the_data).grid(row=3, column=0, sticky=W, padx=10)

# PACKS
login_entry_field.grid(row=1, column=1, sticky=W, pady=10)
password_entry_field.grid(row=2, column=1, sticky=W, pady=10)
# Main Loop
root.mainloop()