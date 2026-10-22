<p align="center">
  <ins><b><kbd>&nbsp;CONSOLE APPLICATION&nbsp;</kbd></b></ins>
</p>

<h1 align="center" style="font-size: 2.5rem; font-weight: 900; color: #1a1a1a; margin-top: 10px; margin-bottom: 10px; border-bottom: none;">
  📋 ADVANCED TASK MANAGER (v1.1)
</h1>

<p align="center">
  <strong>Ein robuster und eleganter Konsolen-Aufgabenmanager mit strukturierter Architektur und JSON-Speicherung.</strong>
  <br />
  <i>Entwickelt mit Python 3 und nativer ANSI-Farbcodierung für eine übersichtliche Aufgabenverwaltung direkt im Terminal.</i>
</p>

<p align="center">
  <a href="#-deutsch">🇩🇪 Deutsch</a> • 
  <a href="#-english">🇺🇸 English</a> • 
  <a href="#-русский">🇷🇺 Русский</a> • 
  <a href="#-українська">🇺🇦 Українська</a>
</p>

---

## 🇩🇪 Deutsch

Die Anwendung bietet ein strukturiertes und intuitives Terminal-Interface zur Verwaltung täglicher Aufgaben. Perfekt optimiert für Entwickler und Administratoren, die ihre To-Dos ohne GUI-Overhead direkt in der Konsole organisieren möchten.

### 🚀 Funktionen
* **Saubere Architektur-Trennung 🏗️**: Vollständige Entkopplung der Business-Logik (`AufgabenManager`) vom UI-Layer (`main`). Das Skript lässt sich dadurch ohne Code-Änderungen in einen Telegram-Bot oder eine GUI portieren.
* **Erweiterte Farbcodierung 🎨**: Statusanzeigen und Systemmeldungen ändern dynamisch ihre Farbe (Grün für Erfolg, Rot für Fehler, Gelb für Infos, Blau für Header) via ANSI-Escapesequenzen.
* **Index-Validierung & Crash-Schutz 🛡️**: Vollständige Absicherung gegen fehlerhafte Benutzereingaben. Ungültige Nummern (z.B. `0`, negative Indizes oder zu große Zahlen) werden abgefangen, ohne dass das Programm abstürzt.
* **Optionale Beschreibungen 📝**: Jede Aufgabe unterstützt neben dem Pflicht-Titel eine optionale, detaillierte Beschreibung für komplexe Workflows.
* **Automatische Daten-Persistenz 💾**: Alle Aufgaben werden in Echtzeit als formatiertes JSON in `tasks.json` gesichert und beim Programmstart automatisch wieder geladen.

### 🛠️ Technologien
* **Framework / Laufzeit**: Python 3.x (Objektorientierte Programmierung)
* **Daten-Persistenz**: Natives `json`-Modul mit UTF-8 Kodierung für reibungslose Sonderzeichen-Unterstützung.
* **System-Schnittstellen**: `os`-Modul zur sicheren Pfad- und Dateiprüfung vor Ladevorgängen.

### 📦 Installation & Ausführung

#### Ausführung aus dem Quellcode
Es wird lediglich eine Standard-Installation von Python 3.x benötigt. Zusätzliche externe Bibliotheken (`pip`) sind nicht erforderlich.

1. Repository klonen:
   ```bash
   git clone https://[github.com](https://github.com/KristinaAlokhina/konsolen-task-manager)
   ```
2. In den Projektordner wechseln:
   ```bash
   cd task-manager
   ```
3. Die Anwendung starten:
   ```bash
   python task_manager.py
   ```

---

## 🇺🇸 English

A structured and lightweight console-based task management utility designed to organize workloads and track daily objectives directly inside your favorite terminal runner.

### 🚀 Features
* **Strict Architecture Separation 🏗️**: Complete boundary isolation between core state logic (`AufgabenManager`) and terminal view rendering (`main`). Built ready to scale into Telegram bots or Tkinter canvases seamlessly.
* **ANSI Color Gamuts 🎨**: High-visibility stream feedback tracking. Outputs change palette structures contextually (Green for success, Red for errors, Yellow for info, Blue for headers).
* **Index & Out-of-Bounds Safeguards 🛡️**: Hardened user input handling. Destructive array calls (such as `0` boundaries or negative offsets) are cleanly validated to maintain zero crash runtime loops.
* **Detailed Task Context 📝**: Supports explicit optional description segments under primary task titles to accommodate complex multi-step item records.
* **Echtzeit Flat-File Pipeline 💾**: Auto-commits internal state tables straight into a local indented `tasks.json` structure using unified UTF-8 schemas.

### 🛠️ Technologies
* **Engine / Runtime**: Python 3.x (Object-Oriented Design)
* **Storage Layer**: Native `json` standard framework equipped with safe ascii escape inhibitors.
* **File Controls**: Core `os` filesystem layer validating active persistence targets dynamically.

### 📦 Installation & Setup

#### Running from Source
Requires a standard Python 3.x execution environment. No external third-party dependencies required.

1. Clone the repository:
   ```bash
   git clone https://[github.com](https://github.com/KristinaAlokhina/konsolen-task-manager)
   ```
2. Navigate to project root:
   ```bash
   cd task-manager
   ```
3. Initialize the manager:
   ```bash
   python task_manager.py
   ```

---

## 🇷🇺 Русский

Компактный и надежный консольный менеджер задач, написанный на Python. Позволяет удобно структурировать списки дел, распределять задачи и просматривать их текущий статус прямо в окне терминала.

### 🚀 Возможности
* **Разделение слоев архитектуры 🏗️**: Бизнес-логика приложения (`AufgabenManager`) полностью отделена от консольного интерфейса (`main`). Это позволяет легко перенести ядро программы в Telegram-бота или десктопное GUI-приложение.
* **Яркая цветовая индикация 🎨**: Интерфейс снабжен понятной цветовой разметкой ANSI (Зеленый — успех, Красный — ошибки, Желтый — уведомления, Голубой — заголовки меню).
* **Защита от некорректного ввода 🛡️**: Программа полностью защищена от случайных ошибок пользователя. Ввод нуля, отрицательных чисел или слишком больших индексов обрабатывается безопасно и не приводит к падению скрипта.
* **Поддержка описаний 📝**: Помимо обязательного заголовка, к каждой задаче можно добавить детальное текстовое описание.
* **Автоматическое сохранение 💾**: Данные записываются в файл `tasks.json` в режиме реального времени с сохранением кодировки UTF-8 и красивыми отступами (indent).

### 🛠️ Технологии
* **Язык**: Python 3.x (Объектно-ориентированный подход)
* **Формат данных**: Встроенный модуль `json` для сериализации объектов в плоские файлы.
* **Проверки ОС**: Родной модуль `os` для безопасной работы с путями и файловой системой.

### 📦 Установка и запуск

#### Запуск из исходного кода
Вам понадобится только установленный интерпретатор Python 3.x. Сторонние библиотеки не требуются.

1. Клонируйте репозиторий:
   ```bash
   git clone https://[github.com](https://github.com/KristinaAlokhina/konsolen-task-manager)
   ```
2. Перейдите в папку проекта:
   ```bash
   cd task-manager
   ```
3. Запустите таск-менеджер:
   ```bash
   python task_manager.py
   ```

---

## 🇺🇦 Українська

Компактний та надійний консольний менеджер завдань, написаний на Python. Дозволяє зручно структурувати списки справ, розподіляти завдання та переглядати їхній поточний статус прямо у вікні термінала.

### 🚀 Можливості
* **Розподіл шарів архітектури 🏗️**: Бізнес-логіка додатка (`AufgabenManager`) повністю відокремлена від консольного інтерфейсу (`main`). Це дозволяє легко перенести ядро програми в Telegram-бота або десктопний GUI-додаток.
* **Яскрава колірна індикація 🎨**: Інтерфейс забезпечений зрозумілою колірною розміткою ANSI (Зелений — успіх, Червоний — помилки, Жовтий — сповіщення, Блакитний — заголовки меню).
* **Захист від некоректного введення 🛡️**: Програма повністю захищена від випадкових помилок користувача. Введення нуля, від'ємних чисел або занадто великих індексів обробляється безпечно і не призводить до падіння скрипта.
* **Підтримка описів 📝**: Крім обов'язкового заголовка, до кожного завдання можна додати детальне текстове опис.
* **Автоматичне збереження 💾**: Дані записуються у файл `tasks.json` у режимі реального часу з збереженням кодування UTF-8 та красивими відступами (indent).

### 🛠️ Технології
* **Мова**: Python 3.x (Об'єктно-орієнтований підхід)
* **Формат даних**: Вбудований модуль `json` для серіалізації об'єктів у плоскі файли.
* **Перевірки ОС**: Рідний модуль `os` для безпечної роботи з шляхами та файловою системою.

### 📦 Встановлення та запуск

#### Запуск із вихідного коду
Вам знадобиться лише встановлений інтерпретатор Python 3.x. Сторонні бібліотеки не потрібні.

1. Клонуйте репозиторій:
   ```bash
   git clone https://[github.com](https://github.com/KristinaAlokhina/konsolen-task-manager)
   ```
2. Перейдіть до папки проєкту:
   ```bash
   cd task-manager
   ```
3. Запустіть таск-менеджер:
   ```bash
   python task_manager.py
   ```
