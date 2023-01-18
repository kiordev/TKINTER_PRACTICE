import tkinter as tk
# Main Config
window = tk.Tk()
window.geometry("500x500")
window.resizable(False, False)
window.config(bg='#473449')
icon = tk.PhotoImage(file='Spartak_Subbota.png')
window.iconphoto(False, icon)

main_label = tk.Label(window,
                      text='''Hello 
world!''',
                      bg = "#0071A9",
                      fg = "white",
                      width=30,
                      height=10,
                      #padx=100,
                      #pady=100,
                      justify=tk.RIGHT,
                      anchor='w'
                      )
main_label.pack()
# Main Loop
window.mainloop()