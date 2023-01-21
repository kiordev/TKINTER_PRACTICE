import tkinter
import tkinter as tk
import customtkinter

def create_label():
    label = tk.Label(window, text="КОЛЯ ПИДОРАС", bg="#8513AF", fg="white")
    label.pack(anchor=tkinter.W, padx=10, pady=10)

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")
window = customtkinter.CTk()
window = customtkinter.CTk(fg_color="#8513AF")

window.geometry("500x500")
window.resizable(False,False)

label_kolya = tk.Label(window, text="КОЛЯ ПИДОРАС", bg="#8513AF", fg="white")

button_kolya = customtkinter.CTkButton(window, text="How is Kolya?", command=create_label)
button_kolya.pack(anchor=tkinter.W, padx=10, pady=10)

window.mainloop()