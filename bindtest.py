import tkinter as tk
from tkinter import ttk

root = tk.Tk()
entry = ttk.Entry(root)  # Hier erstellen wir das Eingabefeld
entry.pack()

def handle_enter(event):
    user_input = entry.get()  # Hole den eingegebenen Text
    print("Benutzereingabe:", user_input)

entry.bind("<Return>", handle_enter)  # Binden der Eingabetaste an die Funktion


root.mainloop()