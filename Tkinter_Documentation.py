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
# window.mainloop() - ВСЕГДА ПИСАТЬ В САМОМ КОНЦЕ

# ---Resolution---
# window.geometry("600x350") # Разрешение окна
# window.resizable(False, False) # Возможность менять размер окна (x, y)
# window.config(bg='#500055') # Цвет заднего фона программы

# ---Icon---
# photo = tk.PhotoImage(file='some_png.png') - подгрузка файла иконки
# window.iconphoto(False,photo) - создание иконки

# ||||Widgets||||
# --- Label ---
# label_1 = tk.Label(window,
#                    text='''Some text''',
#                    bg = '#0071A9', # цвет лабела
#                    fg = 'white', # цвет текста
#                    font = ('Arial', 15, 'bold'), # настройки шрифта
#                    width=20,  1w = 2h # ширина лебла (измеряется в символах = символ(размер, шрифт)
#                    height=10, # высота лебла (измеряется в символах = символ(размер, шрифт)

#                    #padx=20, # отступ текста (работает вместе с anchor)
#                    #pady=30, # отступ текста (работает вместе с anchor)
#                    anchor='n', # прибивка лебла к стороне света s w n e
#                    justify=tk.LEFT # Выравнивание текста по одной линии вертикаль аля "направляющие в корале"
#
#
#                    #relief=tk.RAISED, #Выделение границ
#                    #bd=10, # ширина границы
#
#                    )
# label_1.pack() - для того, чтобы лейбл (появился)
# --- Button---
# counter_button = tk.Button(window,
#                            bg='blue',
#                            fg='white',
#                            text="Counter",
#                            activebackground="purple",
#                            command="some_funtion"
#                            )
# counter_button.pack(anchor='nw',padx=20,pady=30)
