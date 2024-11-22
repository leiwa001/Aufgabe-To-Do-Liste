import json
import tkinter as tk
from pathlib import Path
from time import strftime

from tkcalendar import Calendar


class GUI:
    def __init__(self, fenster):
        super().__init__()

        self.fenster = fenster

        self.dict_list = []

        self.dictionary = {
            "task": "Aufgabe1",
            "completed": False,
            "beschreibung": "Beschreibung:\n\n",
            "faelligkeit": "-nicht festgelegt-",
            "erstellung": "",
        }

        # Fenster erstellen

        # Fenstergröße und Titel festlegen
        self.fenster.geometry("1200x700")
        self.fenster.title("\nDie To-Do-Liste\n")

        # Eingabefeld beschreiben und mit Enter bestätigen
        self.eingabefeld = tk.Entry(self.fenster, bd=3, width=80)
        self.eingabefeld.bind("<Return>", self.callback)

        # Label s.Text
        self.anfangs_label = tk.Label(self.fenster, text="Gib deine Aufgabe ein: ")

        # Label, dass die Aufgabe als gespeichert anzeigt
        self.task_label = tk.Label(self.fenster)

        # Button, um task zu bestätigen
        self.task_button = tk.Button(self.fenster, text="Bestätigen", command=self.button_action_eingabefeld, bd=5)

        # Button, um Daten in Json zu speichern
        self.speicher_button = tk.Button(self.fenster, text="Speichern", command=self.button_action_speichern, bd=5)

        # Button, um Daten aus Json zu laden
        self.lade_button = tk.Button(self.fenster, text="Laden", command=self.button_action_laden, bd=5)

        # Label, um Speichern/Laden zu bestätigen
        self.speicher_label = tk.Label(self.fenster)
        self.lade_label = tk.Label(self.fenster)

        # Exit Button
        self.exit_button = tk.Button(self.fenster, text="Beenden", command=self.fenster.quit, bd=5)

        # Bearbeiten-Button
        self.bearbeiten_button = tk.Button(self.fenster, text="Bearbeiten", command=self.button_action_bearbeiten, bd=5)

        # Auflistung hinzufügen
        self.aufgabenliste = tk.Listbox(self.fenster, width=28, height=28, bd=5)

        self.aufgabenliste.bind("<Double-1>", self.edit_start)

        self.aufgaben_label = tk.Label(self.fenster, text="Deine Aufgaben:")
        self.loesch_button = tk.Button(self.fenster, text="Löschen", command=self.button_action_loeschen, bd=5)
        self.loesch_label = tk.Label(self.fenster)

        # Komponenten zu Fenster hinzufügen und beschreiben
        self.anfangs_label.place(relx=0.05, rely=0.1)
        self.eingabefeld.place(relx=0.2, rely=0.1)
        self.task_label.place(relx=0.36, rely=0.155)
        self.task_button.place(relx=0.41, rely=0.2, width=100, height=40)

        self.speicher_button.place(relx=0.2, rely=0.85, width=100, height=40)
        self.lade_button.place(relx=0.33, rely=0.85, width=100, height=40)
        self.speicher_label.place(relx=0.34, rely=0.45)
        self.lade_label.place(relx=0.36, rely=0.45)

        self.exit_button.place(relx=0.07, rely=0.85, width=100, height=40)

        self.aufgabenliste.place(relx=0.79, rely=0.1)
        self.aufgaben_label.place(relx=0.79, rely=0.06)
        self.loesch_button.place(relx=0.85, rely=0.85, width=100, height=40)
        self.loesch_label.place(relx=0.82, rely=0.92)

        self.bearbeiten_button.place(relx=0.9, rely=0.03, width=100, height=40)

        self.button_action_laden()

        # Funktion für Eingabefeld: Label 'Aufgabe wurde gespeichert', dict erstellen, dict an dict_liste anhängen,

    # eingabefeld zurücksetzen, task in liste anzeigen
    def button_action_eingabefeld(self):
        task = self.eingabefeld.get()
        if task == "":
            self.task_label.config(text="Gib zuerst eine Aufgabe ein!")
        else:
            self.dictionary["task"] = task
            time = strftime("%d.%m.%Y")
            self.dictionary["erstellung"] = time
            new_dict = self.dictionary.copy()
            bestaetigung_task = "Die Aufgabe: '" + task + "' wurde gespeichert."
            self.task_label.config(text=bestaetigung_task)
            self.dict_list.append(new_dict)
            self.eingabefeld.delete(0, tk.END)
            self.aufgabenliste.insert(tk.END, task)
        self.label_loeschen_eingabe()

    # Funktion für Speichern in Json File
    def button_action_speichern(self):
        self.speicher_label.config(text="Ihre Aufgaben wurden gespeichert!")
        path = Path("mylist.json")
        self.task_list = json.dumps(self.dict_list, indent=4)
        path.write_text(self.task_list)
        self.label_loeschen_speichern()

    # Funktion für Laden aus Json File
    def button_action_laden(self):
        self.lade_label.config(text="Ihre Aufgaben wurden geladen!")
        path = Path("mylist.json")
        if path.exists():
            self.task_list = path.read_text()
            self.dict_list = json.loads(self.task_list)
            for wert in self.dict_list:
                task = wert["task"]
                self.aufgabenliste.insert(tk.END, task)
        else:
            print("Keine Aufgaben gespeichert")
        self.label_loeschen_laden()

    # Funktion für Lösch Button
    def button_action_loeschen(self):
        self.loesch_label.config(text="Die ausgewählte Aufgabe\n wurde gelöscht!")
        self.sel_task = self.aufgabenliste.curselection()
        self.aufgabenliste.delete(self.sel_task)
        self.aufgabe_aus_liste_loeschen()

    # löscht ausgewählte aufgabe aus dict_list
    def aufgabe_aus_liste_loeschen(self):
        for i in range(100):
            if self.sel_task == (i,):
                del self.dict_list[i]
        self.label_loeschen_loeschen()

    # mit Enter bestätigen Hilfsfunktion
    def callback(self, event):
        self.button_action_eingabefeld()

    # öffnet Bearbeitung und new_window mit allen button, label, etc.
    def button_action_bearbeiten(self):
        self.new_window = tk.Toplevel(self.fenster)
        self.new_window.geometry("1000x600")

        sel_task = self.aufgabenliste.curselection()

        for i in range(100):
            if sel_task == (i,):
                self.sel_dict = self.dict_list[i]
                task = self.sel_dict["task"]
                beschreibung = self.sel_dict["beschreibung"]

        self.new_window.title(task)

        speicher_button = tk.Button(self.new_window, text="Speichern", command=self.bearbeitung_speichern, bd=5)
        speicher_button.place(relx=0.78, rely=0.85)

        task_label = tk.Label(self.new_window, text=f"Aufgabe: '{task}'", font=("Arial", 20))
        task_label.place(relx=0.42, rely=0.05)

        self.textfeld = tk.Text(self.new_window, height=18, width=30)
        self.textfeld.place(relx=0.7, rely=0.2)
        self.textfeld.insert(tk.END, beschreibung)

        self.cal = Calendar(self.new_window, selectmode="day", year=2024, month=11, day=10, font="Arial 12")
        self.cal.place(relx=0.1, rely=0.48)
        self.cal_button = tk.Button(self.new_window, text="Auswählen", command=self.get_datum, bd=5)
        self.cal_button.place(relx=0.2, rely=0.85)
        self.cal_label = tk.Label(self.new_window, font="Arial 12")
        self.cal_label.place(relx=0.4, rely=0.85)

        erstellt_label = tk.Label(self.new_window, text="Erstellt am: " + self.sel_dict["erstellung"], font="Arial 12")
        erstellt_label.place(relx=0.1, rely=0.18)
        faellig_label = tk.Label(self.new_window, text="Fällig am: " + self.sel_dict["faelligkeit"], font="Arial 12")
        faellig_label.place(relx=0.1, rely=0.25)

        check_status = "  Abgeschlossen!" if self.sel_dict["completed"] else "  Noch nicht abgeschlossen"

        self.check_label = tk.Label(self.new_window, text=check_status, font="Arial 12")
        self.check_label.place(relx=0.11, rely=0.32)

        self.var1 = tk.IntVar()

        self.var1.set(1) if self.sel_dict["completed"] else self.var1.set(0)

        check = tk.Checkbutton(self.new_window, text="", variable=self.var1, onvalue=1, offvalue=0, command=self.checkbox)
        check.place(relx=0.09, rely=0.32)

    # checkbox haken und speichert in dictionary
    def checkbox(self):
        if self.var1.get() == 1:
            self.check_label.config(text="  Abgeschlossen!")
            self.sel_dict["completed"] = True
        else:
            self.check_label.config(text="  Noch nicht erledigt!")
            self.sel_dict["completed"] = False

    # faelligkeitstermin speichern
    def get_datum(self):
        datum = self.cal.get_date()
        self.cal_label.config(text="Fälligkeitstermin: " + self.cal.get_date())
        self.sel_dict["faelligkeit"] = datum

    # speichert Bearbeitung im new_window
    def bearbeitung_speichern(self):
        eingabe = self.textfeld.get("1.0", tk.END)
        self.sel_dict["beschreibung"] = eingabe
        self.new_window.destroy()

        path = Path("mylist.json")
        self.task_list = json.dumps(self.dict_list, indent=4)
        path.write_text(self.task_list)
        self.label_loeschen_speichern()

    # Loesch-Funktionen, um nur 1 Label gleichzeitig anzuzeigen
    def label_loeschen_eingabe(self):
        self.speicher_label.config(text=" ")
        self.lade_label.config(text=" ")
        self.loesch_label.config(text=" ")

    def label_loeschen_speichern(self):
        self.task_label.config(text=" ")
        self.lade_label.config(text=" ")
        self.loesch_label.config(text=" ")

    def label_loeschen_laden(self):
        self.task_label.config(text=" ")
        self.speicher_label.config(text=" ")
        self.loesch_label.config(text=" ")

    def label_loeschen_loeschen(self):
        self.task_label.config(text=" ")
        self.speicher_label.config(text=" ")
        self.lade_label.config(text=" ")

    # Index des zu bearbeitenden Elements
    def edit_start(self, event):
        index = self.aufgabenliste.index(f"@{event.x},{event.y}")
        self.task_edit(index)

    # Einbinden Doppelklick und dann entsprechende Bearbeitung
    def task_edit(self, index):
        self.aufgabenliste.edit_item = index
        text = self.aufgabenliste.get(index)
        y0 = self.aufgabenliste.bbox(index)[1]
        entry = tk.Entry(self.fenster, borderwidth=0, highlightthickness=1)
        entry.bind("<Return>", self.accept_edit)
        entry.bind("<Escape>", self.cancel_edit)

        entry.insert(0, text)
        entry.selection_from(0)
        entry.selection_to("end")
        entry.place(relx=0.8, y=y0 + 70, relwidth=0.2, width=-1)
        entry.focus_set()

    # bei 'ESC' berabeiten abbrechen
    def cancel_edit(self, event):
        event.widget.destroy()

    # bei 'Enter' alten Eintrag löschen und neuen hinzufügen
    def accept_edit(self, event):
        new_data = event.widget.get()
        self.aufgabenliste.delete(self.aufgabenliste.edit_item)
        self.aufgabenliste.insert(self.aufgabenliste.edit_item, new_data)
        event.widget.destroy()


fenster = tk.Tk()

app = GUI(fenster)

fenster.mainloop()
