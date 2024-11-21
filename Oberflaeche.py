import json
import tkinter as tk
from pathlib import Path

dict_list = []

dictionary = {"task": "Aufgabe1", "completed": False, "beschreibung":"Beschreibung:\n\n", "faelligkeit": ""}


# Funktion für Eingabefeld: Label 'Aufgabe wurde gespeichert', dict erstellen, dict an dict_liste anhängen,
# eingabefeld zurücksetzen, task in liste anzeigen
def button_action_eingabefeld():
    global dict_list  # noqa: PLW0602
    task = eingabefeld.get()
    if task == "":
        task_label.config(text="Gib zuerst eine Aufgabe ein!")
    else:
        dictionary["task"] = task
        new_dict = dictionary.copy()
        bestaetigung_task = "Die Aufgabe: '" + task + "' wurde gespeichert."
        task_label.config(text=bestaetigung_task)
        dict_list.append(new_dict)
        print(dict_list)
        eingabefeld.delete(0, tk.END)
        aufgabenliste.insert(tk.END, task)
    label_loeschen_eingabe()


# Funktion für Speichern in Json File
def button_action_speichern():
    speicher_label.config(text="Ihre Aufgaben wurden gespeichert!")
    path = Path("mylist.json")
    task_list = json.dumps(dict_list)
    path.write_text(task_list)
    label_loeschen_speichern()


# Funktion für Laden aus Json File
def button_action_laden():
    global dict_list  # noqa: PLW0603
    lade_label.config(text="Ihre Aufgaben wurden geladen!")
    path = Path("mylist.json")
    if path.exists():
        task_list = path.read_text()
        dict_list = json.loads(task_list)
        print(dict_list)
        for wert in dict_list:
            task = wert["task"]
            aufgabenliste.insert(tk.END, task)
    else:
        print("Keine Aufgaben gespeichert")
    label_loeschen_laden()


# Funktion für Lösch Button
def button_action_loeschen():
    global sel_task  # noqa: PLW0603
    loesch_label.config(text="Die ausgewählte Aufgabe\n wurde gelöscht!")
    sel_task = aufgabenliste.curselection()
    print(sel_task)
    aufgabenliste.delete(sel_task)
    aufgabe_aus_liste_loeschen()


# löscht ausgewählte aufgabe aus dict_list
def aufgabe_aus_liste_loeschen():
    global sel_task  # noqa: PLW0602
    for i in range(100):
        if sel_task == (i,):
            del dict_list[i]
    label_loeschen_loeschen()


# mit Enter bestätigen Hilfsfunktion
def callback(event):
    button_action_eingabefeld()

#öffnet Bearbeitung
def button_action_bearbeiten():
    global x
    sel_task = aufgabenliste.curselection()
    new_window = tk.Toplevel(fenster)
    new_window.geometry("1000x600")
    for i in range(100):
        if sel_task == (i,):
            sel_dict = dict_list[i]
            task = sel_dict['task']
            beschreibung = sel_dict['beschreibung']
    new_window.title(task)
    print(beschreibung)
    print(task)


    speicher_button = tk.Button(new_window, text="Speichern", bd=5)
    speicher_button.place(relx=0.82, rely=0.9)
    task_label = tk.Label(new_window, text=f"Aufgabe: '{task}'", font=("Arial", 20))
    task_label.place(relx=0.42, rely=0.07)

    textfeld = tk.Text(new_window, height=18, width=30)
    textfeld.place(relx=0.7, rely=0.2)
    textfeld.insert(tk.END, beschreibung)

    
        eingabe = textfeld.get("1.0", tk.END)
        sel_dict["beschreibung"]= eingabe
        print(sel_dict)






def label_loeschen_eingabe():
    speicher_label.config(text=" ")
    lade_label.config(text=" ")
    loesch_label.config(text=" ")


def label_loeschen_speichern():
    task_label.config(text=" ")
    lade_label.config(text=" ")
    loesch_label.config(text=" ")


def label_loeschen_laden():
    task_label.config(text=" ")
    speicher_label.config(text=" ")
    loesch_label.config(text=" ")


def label_loeschen_loeschen():
    task_label.config(text=" ")
    speicher_label.config(text=" ")
    lade_label.config(text=" ")


# Index des zu bearbeitenden Element
def edit_start(event):
    index = aufgabenliste.index(f"@{event.x},{event.y}")
    task_edit(index)


# Einbinden Doppelklick und dann entsprechende Bearbeitung
def task_edit(index):
    aufgabenliste.edit_item = index
    text = aufgabenliste.get(index)
    y0 = aufgabenliste.bbox(index)[1]
    entry = tk.Entry(fenster, borderwidth=0, highlightthickness=1)
    entry.bind("<Return>", accept_edit)
    entry.bind("<Escape>", cancel_edit)

    entry.insert(0, text)
    entry.selection_from(0)
    entry.selection_to("end")
    entry.place(relx=0.8, y=y0 + 70, relwidth=0.2, width=-1)
    entry.focus_set()


# bei 'ESC' berabeiten abbrechen
def cancel_edit(event):
    event.widget.destroy()


# bei 'Enter' alten Eintrag löschen und neuen hinzufügen
def accept_edit(event):
    new_data = event.widget.get()
    aufgabenliste.delete(aufgabenliste.edit_item)
    aufgabenliste.insert(aufgabenliste.edit_item, new_data)
    event.widget.destroy()


# Fenster erstellen
fenster = tk.Tk()

# Fenstergröße und Titel festlegen
fenster.geometry("1200x700")
fenster.title("\nDie To-Do-Liste\n")

# Eingabefeld beschreiben und mit Enter bestätigen
eingabefeld = tk.Entry(fenster, bd=3, width=80)
eingabefeld.bind("<Return>", callback)

# Label s.Text
anfangs_label = tk.Label(fenster, text="Gib deine Aufgabe ein: ")

# Label, dass die Aufgabe als gespeichert anzeigt
task_label = tk.Label(fenster)

# Button, um task zu bestätigen
task_button = tk.Button(fenster, text="Bestätigen", command=button_action_eingabefeld, bd=5)

# Button, um Daten in Json zu speichern
speicher_button = tk.Button(fenster, text="Speichern", command=button_action_speichern, bd=5)

# Button, um Daten aus Json zu laden
lade_button = tk.Button(fenster, text="Laden", command=button_action_laden, bd=5)

# Label, um Speichern/Laden zu bestätigen
speicher_label = tk.Label(fenster)
lade_label = tk.Label(fenster)

# Exit Button
exit_button = tk.Button(fenster, text="Beenden", command=fenster.quit, bd=5)

#Bearbeiten-Button
bearbeiten_button = tk.Button(fenster, text="Bearbeiten", command=button_action_bearbeiten, bd=5)

# Auflistung hinzufügen
aufgabenliste = tk.Listbox(fenster, width=28, height=28, bd=5)

aufgabenliste.bind("<Double-1>", edit_start)

aufgaben_label = tk.Label(fenster, text="Deine Aufgaben:")
loesch_button = tk.Button(fenster, text="Löschen", command=button_action_loeschen, bd=5)
loesch_label = tk.Label(fenster)


# Komponenten zu Fenster hinzufügen und beschreiben
anfangs_label.place(relx=0.1, rely=0.1)
eingabefeld.place(relx=0.25, rely=0.1)
task_label.place(relx=0.37, rely=0.2)
task_button.place(relx=0.4, rely=0.25, width=100, height=40)

speicher_button.place(relx=0.25, rely=0.5, width=100, height=40)
lade_button.place(relx=0.5, rely=0.5, width=100, height=40)
speicher_label.place(relx=0.2, rely=0.58)
lade_label.place(relx=0.45, rely=0.58)

exit_button.place(relx=0.375, rely=0.85, width=100, height=40)

aufgabenliste.place(relx=0.8, rely=0.1)
aufgaben_label.place(relx=0.8, rely=0.065)
loesch_button.place(relx=0.85, rely=0.85, width=100, height=40)
loesch_label.place(relx=0.82, rely=0.9)

bearbeiten_button.place(relx=0.7, rely=0.2, width=100, height=40)

button_action_laden()

# Schleife für Betrieb bis Benutzereingabe erfolgt...
fenster.mainloop()

