import json
import os

class Aufgabe:
    """Klasse, die eine einzelne Aufgabe repräsentiert."""
    def __init__(self, titel, beschreibung=""):
        self.titel = titel
        self.beschreibung = beschreibung
        self.ist_erledigt = False

    def als_erledigt_markieren(self):
        """Ändert den Status der Aufgabe auf erledigt."""
        self.ist_erledigt = True

    def to_dict(self):
        """Konvertiert das Aufgaben-Objekt in ein Dictionary für die JSON-Speicherung."""
        return {
            "titel": self.titel,
            "beschreibung": self.beschreibung,
            "ist_erledigt": self.ist_erledigt
        }

    @staticmethod
    def from_dict(daten):
        """Erstellt ein Aufgabe-Objekt aus einem Dictionary."""
        aufgabe = Aufgabe(daten["titel"], daten.get("beschreibung", ""))
        aufgabe.ist_erledigt = daten.get("ist_erledigt", False)
        return aufgabe


class AufgabenManager:
    """Klasse zur Verwaltung der Aufgabenliste (Reine Business-Logik)."""
    def __init__(self, dateiname="tasks.json"):
        self.dateiname = dateiname
        self.aufgaben = self.aufgaben_laden()

    def aufgabe_hinzufuegen(self, titel, beschreibung=""):
        """Fügt eine neue Aufgabe hinzu und speichert die Liste."""
        neue_aufgabe = Aufgabe(titel, beschreibung)
        self.aufgaben.append(neue_aufgabe)
        self.aufgaben_speichern()
        return neue_aufgabe

    def aufgabe_erledigen(self, index):
        """Markiert eine Aufgabe anhand ihrer Nummer als erledigt."""
        # Schutz vor 0, negativen Indizes und Out-of-Bounds
        if index <= 0 or index > len(self.aufgaben):
            return False
        self.aufgaben[index - 1].als_erledigt_markieren()
        self.aufgaben_speichern()
        return True

    def aufgabe_loeschen(self, index):
        """Löscht eine Aufgabe anhand ihrer Nummer aus der Liste."""
        if index <= 0 or index > len(self.aufgaben):
            return None
        entfernte_aufgabe = self.aufgaben.pop(index - 1)
        self.aufgaben_speichern()
        return entfernte_aufgabe

    def aufgaben_speichern(self):
        """Speichert die aktuelle Aufgabenliste in einer JSON-Datei."""
        with open(self.dateiname, "w", encoding="utf-8") as datei:
            json_daten = [aufgabe.to_dict() for aufgabe in self.aufgaben]
            json.dump(json_daten, datei, ensure_ascii=False, indent=4)

    def aufgaben_laden(self):
        """Lädt die Aufgaben aus der JSON-Datei. Gibt bei Fehlern eine leere Liste zurück."""
        if not os.path.exists(self.dateiname):
            return []
        try:
            with open(self.dateiname, "r", encoding="utf-8") as datei:
                json_daten = json.load(datei)
                return [Aufgabe.from_dict(daten) for daten in json_daten]
        except (json.JSONDecodeError, KeyError):
            return []


# Farbcodes für eine schönere Konsolenausgabe
GRUEN = "\033[92m"
ROT = "\033[91m"
GELB = "\033[93m"
BLAU = "\033[96m"
RESET = "\033[0m"

def main():
    """Hauptmenü der Anwendung (Benutzeroberfläche / UI-Layer)."""
    manager = AufgabenManager()

    while True:
        print(f"\n{BLAU}=== KONSOLEN-AUFGABEN-MANAGER ==={RESET}")
        print("1. Aufgaben anzeigen")
        print("2. Aufgabe hinzufügen")
        print("3. Aufgabe als erledigt markieren")
        print("4. Aufgabe löschen")
        print("5. Programm beenden")
        
        auswahl = input("Bitte wählen Sie eine Option (1-5): ").strip()

        if auswahl == "1":
            if not manager.aufgaben:
                print(f"\n{GELB}[INFO] Die Aufgabenliste ist aktuell leer.{RESET}")
                continue
            
            print(f"\n{BLAU}--- IHRE AUFGABEN ---{RESET}")
            for index, aufgabe in enumerate(manager.aufgaben, start=1):
                status = f"{GRUEN}[X] Erledigt{RESET}" if aufgabe.ist_erledigt else f"{ROT}[ ] Offen{RESET}"
                print(f"{index}. {aufgabe.titel} - {status}")
                if aufgabe.beschreibung:
                    print(f"   Beschreibung: {aufgabe.beschreibung}")
            print(f"{BLAU}---------------------{RESET}")

        elif auswahl == "2":
            titel = input("Titel der Aufgabe: ").strip()
            if not titel:
                print(f"\n{ROT}[FEHLER] Der Titel darf nicht leer sein!{RESET}")
                continue
            beschreibung = input("Beschreibung (optional): ").strip()
            manager.aufgabe_hinzufuegen(titel, beschreibung)
            print(f"\n{GRUEN}[ERFOLG] Aufgabe '{titel}' wurde erfolgreich hinzugefügt!{RESET}")

        elif auswahl == "3":
            if not manager.aufgaben:
                print(f"\n{GELB}[INFO] Keine Aufgaben zum Bearbeiten vorhanden.{RESET}")
                continue
            try:
                nummer = int(input("Nummer der zu erledigenden Aufgabe: "))
                if manager.aufgabe_erledigen(nummer):
                    print(f"\n{GRUEN}[ERFOLG] Aufgabe Nr. {nummer} wurde als erledigt markiert!{RESET}")
                else:
                    print(f"\n{ROT}[FEHLER] Ungültige Aufgabennummer!{RESET}")
            except ValueError:
                print(f"\n{ROT}[FEHLER] Bitte geben Sie eine gültige Zahl ein!{RESET}")

        elif auswahl == "4":
            if not manager.aufgaben:
                print(f"\n{GELB}[INFO] Keine Aufgaben zum Löschen vorhanden.{RESET}")
                continue
            try:
                nummer = int(input("Nummer der zu löschenden Aufgabe: "))
                entfernte_aufgabe = manager.aufgabe_loeschen(nummer)
                if entfernte_aufgabe:
                    print(f"\n{GRUEN}[ERFOLG] Aufgabe '{entfernte_aufgabe.titel}' wurde gelöscht!{RESET}")
                else:
                    print(f"\n{ROT}[FEHLER] Ungültige Aufgabennummer!{RESET}")
            except ValueError:
                print(f"\n{ROT}[FEHLER] Bitte geben Sie eine gültige Zahl ein!{RESET}")

        elif auswahl == "5":
            print("\nAuf Wiedersehen! Vielen Dank für die Nutzung.")
            break
        else:
            print(f"\n{ROT}[FEHLER] Ungültige Auswahl, bitte versuchen Sie es erneut.{RESET}")


if __name__ == "__main__":
    main()
