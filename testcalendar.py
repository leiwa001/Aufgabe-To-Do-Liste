import tkinter as tk   
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText 


window = tk.Tk()
window.geometry("800x800")

frame_title = tk.Frame(window)
frame_title.pack(fill='both', expand=True, pady=5, padx=5)

listbox_title = tk.Listbox(frame_title, selectbackground="#960000", selectforeground="white", bg="white", width = 50, height = 20)
listbox_title.place(x=1, y=1)
listbox_title.configure(font=("Arial", 12))

## Vertical Scroll Bar ##
scrollbar_title = tk.Scrollbar(frame_title, command=listbox_title.yview, orient="vertical")
listbox_title.config(yscrollcommand=scrollbar_title.set)
scrollbar_title.place(in_=listbox_title, relx=1.0, relheight=1.0, bordermode="outside")

listbox_title.bind('<Double-Button-1>') 


text_download = ScrolledText(window, bg="white", width = 50, height = 10)
text_download.place(x=1, y=500)
text_download.configure(font=("Arial", 14))


window.mainloop()