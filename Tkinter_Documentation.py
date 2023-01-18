#######################################
# Техническая документация для практики по Tkinter
# Создатель: Александр Киор
# Дата: 18.01.2023
# Дипломный проект по Python
#######################################

# ||||Main Rules||||
# ---Main---
# import tkinter as tk # импорт библиотеки tkinter, и создание псевдо для него
# window = tk.Tk() # Создание окна
# window.title("KPT quastions") # Создание названия окна
# # !!!Главный цикл!!!
# window.mainloop()

# ---Resolution---
# window.geometry("600x350") # Разрешение окна
# window.resizable(False, False) # Возможность менять размер окна (x, y)
# window.config(bg='#500055') # Цвет заднего фона программы

# # ---Icon---
# photo = tk.PhotoImage(file='some_png.png') - подгрузка файла иконки
# window.iconphoto(False,photo) - создание иконки
