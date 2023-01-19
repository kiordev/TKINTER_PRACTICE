import tkinter
import tkinter as tk
import customtkinter
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
#Main_Window_Option
main_window = customtkinter.CTk()
main_window = customtkinter.CTk(fg_color="#382441")
main_window.resizable(False, False)
main_window.geometry("500x500")


#Виджеты
main_name_label = tk.Label(main_window,text="Hello world!", #Hello world Label
                           bg="#382441",
                           fg="white",
                           font=("Arial",20,"bold")
                           )
button_left = customtkinter.CTkButton(master=main_window,
                        text="Left Button",
                        fg_color="#00655E",
                        hover_color="#00CDBF"
                        )
button_center = customtkinter.CTkButton(master=main_window,
                        text="Center Button",
                        fg_color="#00655E",
                        hover_color="#00CDBF"
                        )
button_right = customtkinter.CTkButton(master=main_window,
                        text="Right Button",
                        fg_color="#00655E",
                        hover_color="#00CDBF"
                        )
# Запуск виджетов
main_name_label.pack(anchor='nw', padx=5, pady=10)
button_left.pack(anchor=tkinter.NW, padx=10, pady=10)
button_center.pack(anchor=tkinter.NW, padx=10, pady=10)
button_right.pack(anchor=tkinter.NW, padx=10, pady=10)

main_window.mainloop()

# import tkinter
# import customtkinter
#
# customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
#
# app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.geometry("400x240")
#
# def button_function():
#     print("button pressed")
#
# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
#
# app.mainloop()