import tkinter as tk

root = tk.Tk()

def ausgabe():
    print(checkbox01var.get())
    aktuell_ausgewaehlt = checkbox01var.get()
    textausgabe = tk.Label(root, text=aktuell_ausgewaehlt, bg="orange")
    textausgabe.pack()

checkbox01 = tk.Checkbutton(root)
checkbox01["text"] = "Sport treiben"
checkbox01.pack()

checkbox01var = tk.BooleanVar()
checkbox01var.set(True)
checkbox01["variable"] = checkbox01var

checkbox02 = tk.Checkbutton(root)
checkbox02["text"] = "Lesen"
checkbox02.pack()

checkbox02var = tk.BooleanVar()
checkbox02["variable"] = checkbox02var

checkbox03 = tk.Checkbutton(root)
checkbox03["text"] = "Filme schauen"
checkbox03.pack()

checkbox03var = tk.BooleanVar()
checkbox03["variable"] = checkbox03var

schaltf1 = tk.Button(root, text="Aktion durchführen", command= ausgabe)
schaltf1.pack()

root.mainloop()
