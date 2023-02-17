import os
import shutil
import tkinter as tk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Suchverzeichnis auswählen
        self.search_dir_label = tk.Label(self, text="Suchverzeichnis:")
        self.search_dir_label.pack(side="top")
        self.search_dir = tk.StringVar()
        self.search_dir.set("")
        self.search_dir_button = tk.Button(self, text="Durchsuchen", command=self.choose_search_dir)
        self.search_dir_button.pack(side="top")
        self.search_dir_entry = tk.Entry(self, textvariable=self.search_dir)
        self.search_dir_entry.pack(side="top")

        # Zielverzeichnis auswählen
        self.dest_dir_label = tk.Label(self, text="Zielverzeichnis:")
        self.dest_dir_label.pack(side="top")
        self.dest_dir = tk.StringVar()
        self.dest_dir.set("")
        self.dest_dir_button = tk.Button(self, text="Durchsuchen", command=self.choose_dest_dir)
        self.dest_dir_button.pack(side="top")
        self.dest_dir_entry = tk.Entry(self, textvariable=self.dest_dir)
        self.dest_dir_entry.pack(side="top")

        # Start Button
        self.start_button = tk.Button(self, text="Start", command=self.start_move_files)
        self.start_button.pack(side="top")

        # Fortschrittsanzeige
        self.progress_label = tk.Label(self, text="Fortschritt:")
        self.progress_label.pack(side="top")
        self.progress = tk.StringVar()
        self.progress.set("Bereit.")
        self.progress_display = tk.Label(self, textvariable=self.progress)
        self.progress_display.pack(side="top")

    def choose_search_dir(self):
        # Suchverzeichnis auswählen
        self.search_dir.set(filedialog.askdirectory())

    def choose_dest_dir(self):
        # Zielverzeichnis auswählen
        self.dest_dir.set(filedialog.askdirectory())

    def start_move_files(self):
        # Verzeichnisse aus den Entry-Feldern lesen
        search_dir = self.search_dir.get()
        dest_dir = self.dest_dir.get()

        # Prüfen, ob die Verzeichnisse leer sind
        if not search_dir or not dest_dir:
            self.progress.set("Bitte wählen Sie Such- und Zielverzeichnisse aus.")
            return

        # Erstelle den neuen Ordner, wenn er nicht bereits existiert
        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir)

        # Durchsuche das Verzeichnis nach Dateien mit "(2)" im Namen und verschiebe sie
        files_to_move = [filename for filename in os.listdir(search_dir) if "(2)" in filename]
        num_files = len(files_to_move)
        for i, filename in enumerate(files_to_move):
            src = os.path.join(search_dir, filename)
            dst = os.path.join(dest_dir, filename)
            shutil.move(src, dst)
            self.progress.set(f"Verschiebe {i+1}/{num_files} Dateien.")
            self.update_idletasks()

        self.progress.set("Verschieben abgeschlossen.")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
