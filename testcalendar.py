import tkinter as tk
from tkinter import simpledialog

def on_double_click(event):
    item = listbox.get(listbox.curselection())
    new_value = simpledialog.askstring("Eingabe", f"Ändere den Wert:", initialvalue=item)
    if new_value:
        listbox.delete(listbox.curselection())
        listbox.insert(tk.ACTIVE, new_value)

root = tk.Tk()
root.title("Doppelklick zum Bearbeiten")

listbox = tk.Listbox(root)
listbox.pack()

# Füge einige Elemente zur Liste hinzu
items = ["Element 1", "Element 2", "Element 3", "Element 4"]
for item in items:
    listbox.insert(tk.END, item)

listbox.bind("<Double-1>", on_double_click)

root.mainloop()