# Selenium Software Testing Projekt

## 📌 Projektbeschreibung

Dieses Projekt ist ein automatisiertes Softwaretesting-Projekt für eine webbasierte E-Commerce-Anwendung.

Ziel des Projekts ist es, wichtige Benutzerfunktionen zu testen und automatisierte Tests mit **Python, Selenium WebDriver und pytest** zu entwickeln.

Der Schwerpunkt liegt auf funktionalen UI-Tests, positiven und negativen Testszenarien sowie der Dokumentation und Nachverfolgung von Testergebnissen und Fehlern.

---

## 🎯 Testziele

Im Rahmen dieses Projekts werden unter anderem folgende Funktionen getestet:

* Benutzerregistrierung
* Benutzer-Login
* Produktauswahl
* Hinzufügen von Produkten zum Warenkorb
* Überprüfung des Warenkorbs
* Kaufprozess
* Positive und negative Testszenarien

---

## 🛠️ Technologien und Tools

* **Python**
* **Selenium WebDriver**
* **pytest**
* **Git**
* **GitHub**
* **Jira**
* **Chrome**

---

## 📁 Projektstruktur

```text
selenium-software-testing/
│
├── tests/
│   ├── test_login.py
│   ├── test_registration.py
│   ├── test_products.py
│   └── test_logout.py
│
├── test-cases/
│   ├── login-test-cases.md
│   ├── registration-test-cases.md
│   └── product-test-cases.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧪 Automatisierte Tests

### 🔐 Login

Die Login-Tests überprüfen unter anderem:

* Login mit gültigen Zugangsdaten
* Login mit ungültigen Zugangsdaten
* Login mit einem nicht registrierten Benutzer
* Prüfung der Pflichtfelder
* Weiterleitung nach erfolgreichem Login

### 📝 Registrierung

Die Registrierungstests überprüfen unter anderem:

* Registrierung mit gültigen Daten
* Prüfung der Pflichtfelder
* Ungültige username
* Ungültiges Passwort
* Registrierung mit bereits verwendeter Username

### 🛒 Produkte und Warenkorb

Die Produkttests überprüfen unter anderem:

* Anzeige der verfügbaren Produkte
* Auswahl eines Produkts
* Anzeige der Produktdetails
* Hinzufügen eines Produkts zum Warenkorb
* Überprüfung des Warenkorbs
* Änderung der Produktmenge

### 💳 Kaufprozess

Der Kaufprozess nach erfolgreicher Authentifizierung wird ebenfalls getestet:

* Auswahl eines Produkts
* Hinzufügen zum Warenkorb
* Überprüfung des Warenkorbs
* Start des Checkout-Prozesses
* Abschluss des Kaufvorgangs
* Überprüfung der Bestätigung
---

## 📋 Testfälle

Die manuellen Testfälle sind im Verzeichnis `test-cases/` dokumentiert.

Die Testfälle enthalten sowohl **positive als auch negative Testszenarien**.

Beispiele:

* Login mit gültigen Zugangsdaten
* Login mit falschem Passwort
* Registrierung mit gültigen Daten
* Registrierung mit ungültiger Username
* Pflichtfelder
* Produkt zum Warenkorb hinzufügen
* Produkt aus dem Warenkorb entfernen

---

## ⚙️ Installation

### 1. Repository klonen

```bash
git clone https://github.com/sumak-hash/web-application-testing.git
```

### 2. Projekt öffnen

Das Projekt kann beispielsweise mit **Visual Studio code** geöffnet werden.

### 3. Virtuelle Umgebung erstellen

```bash
python -m venv .venv
```

### 4. Virtuelle Umgebung unter Windows aktivieren

```bash
.venv\Scripts\activate
```

### 5. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

---

## ▶️ Tests ausführen

Alle automatisierten Tests ausführen:

```bash
pytest
```

Tests mit detaillierter Ausgabe ausführen:

```bash
pytest -v
```

Nur die Login-Tests ausführen:

```bash
pytest tests/test_login.py
```

Nur die Registrierungstests ausführen:

```bash
pytest tests/test_registration.py
```

---

## 📊 Testergebnisse

Die Testergebnisse werden nach jedem Testlauf überprüft.

Beispiel:

```text
============================= test session starts =============================

tests/test_login.py          PASSED
tests/test_registration.py   PASSED
tests/test_products.py       PASSED
tests/test_logout.py         PASSED

============================== 4 passed ==============================
```

Bei einem fehlgeschlagenen Test wird die Ursache analysiert.

Wenn ein tatsächlicher Fehler in der Anwendung festgestellt wird, wird ein entsprechender **Bug in Jira** erstellt.

---

## 🐞 Bug-Reporting

Fehler werden in **Jira** dokumentiert und verwaltet.

Ein Bug-Report enthält beispielsweise:

* Zusammenfassung
* Beschreibung
* Voraussetzungen
* Schritte zur Reproduktion
* Erwartetes Ergebnis
* Tatsächliches Ergebnis
* Priorität
* Testumgebung
* Screenshots oder andere Nachweise

---

## 🔄 Git-, GitHub- und Jira-Workflow

Für die Verwaltung des Projekts werden **Git, GitHub und Jira** verwendet.

Der typische Workflow sieht folgendermaßen aus:

```text
Jira-Aufgabe
      ↓
Git-Branch erstellen
      ↓
Tests entwickeln / ändern
      ↓
Tests mit pytest ausführen
      ↓
Git Commit
      ↓
Git Push
      ↓
GitHub
      ↓
Pull Request
      ↓
Jira aktualisieren
```

Die Jira-Task-ID wird in den Commit-Nachrichten verwendet.

Beispiel:

```bash
git commit -m "QA-25 Add authenticated product purchase tests"
```

Dadurch kann der Commit der entsprechenden Jira-Aufgabe zugeordnet werden.

---

## 🌿 Branching

Für neue Funktionen oder Testbereiche werden separate Git-Branches verwendet.

Beispiel:

```text
main
│
├── feature/QA-15-login-tests
├── feature/QA-16-registration-tests
└── feature/QA-25-product-purchase-tests
```

Die Änderungen werden nach erfolgreicher Prüfung über einen Pull Request in den `main`-Branch integriert.

---

## 🧰 Verwendete Testing-Techniken

In diesem Projekt werden unter anderem folgende Techniken eingesetzt:

* Funktionales Testing
* UI Testing
* Positive Tests
* Negative Tests
* Test Case Design
* Testautomatisierung
* Selenium WebDriver
* pytest
* Assertions
* Robuste Locators
* `WebDriverWait`
* Fehleranalyse
* Bug Reporting

---

## 📚 Lernziele

Mit diesem Projekt werden praktische Kenntnisse in folgenden Bereichen aufgebaut:

* Entwicklung automatisierter UI-Tests
* Strukturierung von Testfällen
* Durchführung von positiven und negativen Tests
* Analyse von Testergebnissen
* Dokumentation von Fehlern
* Arbeiten mit Jira
* Versionsverwaltung mit Git
* Zusammenarbeit mit GitHub
* Branching und Pull Requests

---

## 🚀 Geplante Erweiterungen

Das Projekt kann zukünftig erweitert werden durch:

* Page Object Model (POM)
* Weitere positive und negative Tests
* Zentrale Testdatenverwaltung
* Automatische Screenshots bei fehlgeschlagenen Tests
* HTML-Testreports
* Continuous Integration mit GitHub Actions
* Erweiterte Jira-Integration
* Automatisierte Regressionstests

---

## 👩‍💻 Autorin

**Suzanne Lora Makoutchoup Tene**

**Software Testing / QA Automation**

Technologien:

`Python` · `Selenium` · `pytest` · `Jira` · `Git` · `GitHub`
