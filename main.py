import tkinter as tk
#Main_Window_Option
main_window = tk.Tk()
main_window.resizable(False, False)
main_window.geometry("500x500")
main_window.config(bg="#55324D")
icon = tk.PhotoImage(file='some_png.png')
main_window.iconphoto(False,icon)

#Виджеты
main_name_label = tk.Label(main_window,text="Hello world!", #Hello world Label
                           bg="#55324D",
                           fg="white",
                           font=("Arial",20,"bold")
                           )
button_left = tk.Button(main_window,
                        text="Left Button",
                        bg="#CD00FF",
                        fg="#00FFFF")
button_center = tk.Button(main_window,
                        text="Center Button",
                        bg="#CD00FF",
                        fg="#00FFFF")
button_right = tk.Button(main_window,
                        text="Right Button",
                        bg="#CD00FF",
                        fg="#00FFFF")
# Запуск виджетов
main_name_label.pack(anchor='nw', padx=5, pady=10)
button_left.pack(anchor="nw", padx=10, pady=10)
button_center.pack(anchor="nw", padx=10, pady=10)
button_right.pack(anchor="nw", padx=10, pady=10)

main_window.mainloop()