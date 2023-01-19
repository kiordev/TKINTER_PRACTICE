import tkinter as tk

win = tk.Tk()
win.geometry("500x500")
win.resizable(False,False)
icon = tk.PhotoImage(file='icon.png')
win.iconphoto(True,icon)
win.config(bg="#150035")
win.title("Test grid")

#Пример цикла для создания колонок
for i in range(5):
    for j in range(2):
        tk.Button(win,text=f" Button: {i} {j}", bg="blue", fg="white").grid(row=i, column=j, stick="w")

# win.columnconfigure(0,minsize=100)
# win.columnconfigure(1,minsize=100)



win.mainloop()