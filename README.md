# Konsolen-Task-Manager (Command-Line Task Manager)

<p align="center">
  <a href="#-deutsch">Deutsch</a> • 
  <a href="#-english">English</a>
</p>

---

## 🇩🇪 Deutsch

### 🚀 Funktionen
* **Vollständige CRUD-Operationen**: Nahtloses Erstellen, Lesen, Aktualisieren (als erledigt markieren) und Löschen von Aufgaben in Echtzeit.
* **Intelligente Fehlerbehandlung**: Robust gegen ungültige Benutzereingaben (z. B. Buchstaben statt Zahlen oder leere Titel) durch strukturierte `try-except`-Logik.
* **Persistente Speicherung**: Alle Daten bleiben durch automatische Serialisierung im JSON-Format auch nach dem Schließen der Anwendung vollständig erhalten.
* **Saubere Menüführung**: Ein interaktives und übersichtliches Textmenü in der Kommandozeile führt den Benutzer intuitiv durch alle Funktionen.
* **Strukturierter Code**: Konsistente Umsetzung von objektorientierter Programmierung (OOP) mit getrennten Klassen für Aufgaben und Verwaltung.

### 🛠️ Technologien
* Python 3.10+
* Architekturmuster: **OOP** (Objektorientierte Programmierung)
* Datenformat: **JSON** für die Daten-Persistenz
* Kernmodule: `json` und `os` (Python Standardbibliothek)

### 📂 Struktur der Benutzeroberfläche
Die Anwendung läuft vollständig in der Konsole und ist wie folgt aufgeteilt:
* **Hauptmenü**: Eine nummerierte Auswahlliste (1–5) zur Steuerung aller Kernfunktionen der Anwendung.
* **Aufgaben-Übersicht**: Eine dynamische Liste, die alle aktuellen Aufgaben mit ID, Titel, optionaler Beschreibung und dem aktuellen Status (`[ ] Offen` / `[X] Erledigt`) anzeigt.

### 📦 Installation & Ausführung

#### Option 1: Schneller Start über CLI
Für die Ausführung wird lediglich eine installierte Python-Umgebung benötigt:
1. Repository klonen:
   ```bash
   git clone https://github.com/KristinaAlokhina/konsolen-task-manager
   ```
2. In den Projektordner wechseln:
   ```bash
   cd konsolen-task-manager
   ```
3. Anwendung ausführen:
   ```bash
   python task_manager.py
   ```

---

## 🇺🇸 English

### 🚀 Features
* **Full CRUD Operations**: Seamless real-time creation, reading, updating (marking as completed), and deletion of tasks.
* **Smart Error Handling**: Robust defense against invalid user entries (e.g., text instead of numbers or empty titles) using structured `try-except` blocks.
* **Persistent Data**: All task records are securely stored locally in JSON format and remain intact after closing the application.
* **Clean CLI Navigation**: An interactive and intuitive text-based command-line menu guides the user smoothly through all operations.
* **Structured Codebase**: Solid implementation of Object-Oriented Programming (OOP) with dedicated classes for task models and manager logic.

### 🛠️ Technologies
* Python 3.10+
* Design Pattern: **OOP** (Object-Oriented Programming)
* Data Format: **JSON** for persistent storage
* Core Modules: `json` and `os` (Python Standard Library)

### 📂 User Interface Structure
The application runs entirely in the terminal and features the following sections:
* **Main Menu**: A numbered control panel (1–5) to execute all core actions within the application.
* **Task Overview**: A dynamic interface listing all current items with their ID, title, optional description, and real-time status (`[ ] Offen` / `[X] Erledigt`).

### 📦 Installation & Setup

#### Option 1: Run from Command Line
Only a local Python installation is required to run this application:
1. Clone the repository:
   ```bash
   git clone https://github.com/KristinaAlokhina/konsolen-task-manager
   ```
2. Navigate to the project directory:
   ```bash
   cd konsolen-task-manager
   ```
3. Build and run the application:
   ```bash
   python task_manager.py
   ```
