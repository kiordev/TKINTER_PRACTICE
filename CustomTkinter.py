import tkinter as tk
from tkinter import LEFT, W

import customtkinter

# Main Window Settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk(fg_color="#3C143C")
root.geometry("300x300")
root.resizable(False, False)
root.title("Custom Entry Test")

login_entry_field = tk.Entry(root)
login_entry_field.grid()

print(login_entry_field.get())
root.mainloop()
