import tkinter as tk

from pathlib import Path
import json

dict_list = []

dict = {
    'task'      :   'Aufgabe1',
    'completed' :    False
}

#Funktion für Eingabefeld: Label 'Aufgabe wurde gespeichert', dict erstellen, dict an dict_liste anhängen, eingabefeld zurücksetzen, task in liste anzeigen
def button_action_eingabefeld():
    task = eingabefeld.get()
    if(task == ""):
        task_label.config(text = "Gib zuerst eine Aufgabe ein!")
    else:
        dict['task'] = task
        new_dict = dict.copy()
        bestaetigung_task = "Die Aufgabe: '" + task + "' wurde gespeichert."
        task_label.config(text = bestaetigung_task)
        dict_list.append(new_dict)
        print(dict_list)
        eingabefeld.delete(0,tk.END)
        aufgabenliste.insert(tk.END, task)

#Funktion für Speichern in Json File
def button_action_speichern():
    speicher_label.config(text = "Ich speicher!")
    path = Path('mylist.json')
    task_list =json.dumps(dict_list)
    path.write_text(task_list)    

#Funktion für Laden aus Json File
def button_action_laden():
    lade_label.config(text = "Ich lade!")

#Funktion für Lösch Button
def button_action_loeschen():
    loesch_label.config(text = "Ich lösche!")

#mit Enter bestätigen Hilfsfunktion        
def callback(event):
    button_action_eingabefeld()


#Fenster erstellen
fenster = tk.Tk()

#Fenstergröße und Titel festlegen
fenster.geometry("1200x700")
fenster.title("\nDie To-Do-Liste\n")

#Eingabefeld beschreiben und mit Enter bestätigen
eingabefeld = tk.Entry(fenster, bd=3, width=80)
eingabefeld.bind("<Return>", callback)

#Label s.Text
anfangs_label = tk.Label(fenster, text="Gib deine Aufgabe ein: ")

#Label, dass die Aufgabe als gespeichert anzeigt
task_label = tk.Label(fenster)

#Button, um task zu bestätigen
task_button = tk.Button(fenster, text="Bestätigen", command = button_action_eingabefeld, bd=5)

#Button, um Daten in Json zu speichern
speicher_button = tk.Button(fenster, text="Speichern", command = button_action_speichern, bd=5)

#Button, um Daten aus Json zu laden
lade_button = tk.Button(fenster, text="Laden", command = button_action_laden, bd=5)

#Label, um Speichern/Laden zu bestätigen
speicher_label = tk.Label(fenster)
lade_label = tk.Label(fenster)

#Exit Button
exit_button = tk.Button(fenster, text="Beenden", command = fenster.quit, bd=5)

#Auflistung hinzufügen
aufgabenliste = tk.Listbox(fenster, width = 38, height = 32)

aufgaben_label = tk.Label(fenster, text="Deine Aufgaben:")
loesch_button = tk.Button(fenster, text="Löschen", command = button_action_loeschen, bd=5)
loesch_label = tk.Label(fenster)


#Komponenten zu Fenster hinzufügen und beschreiben
anfangs_label.place(relx = 0.1, rely = 0.1)
eingabefeld.place(relx = 0.25, rely = 0.1)
task_label.place(relx = 0.37, rely = 0.2)
task_button.place(relx = 0.4, rely = 0.25, width = 100, height = 40)

speicher_button.place(relx = 0.15, rely = 0.7, width = 100, height = 40)
lade_button.place(relx = 0.6, rely = 0.7, width = 100, height = 40)
speicher_label.place(relx = 0.15, rely = 0.78)
lade_label.place(relx = 0.6, rely = 0.78)

exit_button.place(relx = 0.375, rely = 0.85, width = 100, height = 40)

aufgabenliste.place(relx = 0.78, rely = 0.1)
aufgaben_label.place(relx = 0.78, rely = 0.065)
loesch_button.place(relx = 0.85, rely = 0.85, width = 100, height = 40)
loesch_label.place(relx = 0.78, rely = 0.85)


#Schleife für Betrieb bis Benutzereingabe erfolgt...
fenster.mainloop()
