import json
import os

class Task:
    """Klasse, die eine einzelne Aufgabe repräsentiert."""
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def to_dict(self):
        """Konvertiert das Objekt in ein Dictionary für die JSON-Speicherung."""
        return {
            "title": self.title,
            "description": self.description,
            "is_completed": self.is_completed
        }

    @staticmethod
    def from_dict(data):
        """Erstellt ein Task-Objekt aus einem Dictionary."""
        task = Task(data["title"], data["description"])
        task.is_completed = data["is_completed"]
        return task


class TaskManager:
    """Klasse zur Verwaltung der Aufgabenliste."""
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def add_task(self, title, description=""):
        """Fügt eine neue Aufgabe hinzu."""
        new_task = Task(title, description)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"\n[ERFOLG] Aufgabe '{title}' wurde erfolgreich hinzugefügt!")

    def show_tasks(self):
        """Zeigt alle Aufgaben an."""
        if not self.tasks:
            print("\n[INFO] Die Aufgabenliste ist aktuell leer.")
            return

        print("\n--- IHRE AUFGABEN ---")
        for index, task in enumerate(self.tasks, start=1):
            status = "[X] Erledigt" if task.is_completed else "[ ] Offen"
            print(f"{index}. {task.title} - {status}")
            if task.description:
                print(f"   Beschreibung: {task.description}")
        print("---------------------")

    def complete_task(self, index):
        """Markiert eine Aufgabe als erledigt."""
        try:
            self.tasks[index - 1].mark_as_completed()
            self.save_tasks()
            print(f"\n[ERFOLG] Aufgabe Nr. {index} wurde als erledigt markiert!")
        except IndexError:
            print("\n[FEHLER] Ungültige Aufgabennummer!")

    def delete_task(self, index):
        """Löscht eine Aufgabe aus der Liste."""
        try:
            removed = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"\n[ERFOLG] Aufgabe '{removed.title}' wurde gelöscht!")
        except IndexError:
            print("\n[FEHLER] Ungültige Aufgabennummer!")

    def save_tasks(self):
        """Speichert die Aufgaben in einer JSON-Datei."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json_data = [task.to_dict() for task in self.tasks]
            json.dump(json_data, file, ensure_ascii=False, indent=4)

    def load_tasks(self):
        """Lädt die Aufgaben aus einer JSON-Datei."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                json_data = json.load(file)
                return [Task.from_dict(data) for data in json_data]
        except (json.JSONDecodeError, KeyError):
            print("\n[WARNUNG] Fehler beim Laden der Datei. Eine neue Liste wird erstellt.")
            return []


def main():
    """Hauptmenü der Anwendung."""
    manager = TaskManager()

    while True:
        print("\n=== KONSOLEN-TASK-MANAGER ===")
        print("1. Aufgaben anzeigen")
        print("2. Aufgabe hinzufügen")
        print("3. Aufgabe als erledigt markieren")
        print("4. Aufgabe löschen")
        print("5. Programm beenden")
        
        auswahl = input("Bitte wählen Sie eine Option (1-5): ").strip()

        if auswahl == "1":
            manager.show_tasks()
        elif auswahl == "2":
            title = input("Titel der Aufgabe: ").strip()
            if not title:
                print("\n[FEHLER] Der Titel darf nicht leer sein!")
                continue
            description = input("Beschreibung (optional): ").strip()
            manager.add_task(title, description)
        elif auswahl == "3":
            manager.show_tasks()
            if manager.tasks:
                try:
                    num = int(input("Nummer der zu erledigenden Aufgabe: "))
                    manager.complete_task(num)
                except ValueError:
                    print("\n[FEHLER] Bitte geben Sie eine gültige Zahl ein!")
        elif auswahl == "4":
            manager.show_tasks()
            if manager.tasks:
                try:
                    num = int(input("Nummer der zu löschenden Aufgabe: "))
                    manager.delete_task(num)
                except ValueError:
                    print("\n[FEHLER] Bitte geben Sie eine gültige Zahl ein!")
        elif auswahl == "5":
            print("\nAuf Wiedersehen! Vielen Dank für die Nutzung.")
            break
        else:
            print("\n[FEHLER] Ungültige Auswahl, bitte versuchen Sie es erneut.")


if __name__ == "__main__":
    main()
