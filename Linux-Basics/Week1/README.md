# 🐧 Woche 1: Linux Foundation & Installation

> **Status:** 🟡 In Arbeit (Theorie-Phase)
> **System:** Ubuntu 24.04 LTS (geplant für Dual-Boot)

## 🎯 Lernziele dieser Woche
- [ ] Architektur von Linux verstehen (Kernel, Shell, User-Space)
- [ ] Das Dateisystem (File System Hierarchy) kennenlernen
- [ ] Vorbereitung der Installation (Partitionierung)

---

## 📚 Theorie-Journal (Heute gelernt)

Bevor ich das System installiere, habe ich mich mit der Struktur von Linux befasst. Anders als bei Windows (Laufwerk C:\) gibt es bei Linux einen einzigen Verzeichnisbaum, der bei `/` (Root) beginnt.

### 📂 Das Dateisystem erklärt
Ich habe recherchiert, wofür die wichtigsten System-Ordner zuständig sind:

* **`/` (Root Verzeichnis):**
  * ... (Schreibe hier: Was ist das? Der Startpunkt von allem?)

* **`/home`:**
  * ... (Wer hat hier seine Dateien? Ähnlich wie "C:\Users" bei Windows?)

* **`/etc`:**
  * ... (Tipp: Hier liegen Konfigurationsdateien. "Editable Text Configuration"?)

* **`/var`:**
  * ... (Steht für "Variable". Was liegt hier? Logs? Webseiten?)

* **`/bin` & `/usr/bin`:**
  * ... (Tipp: Hier liegen die Befehle/Programme, die ich im Terminal nutze.)

* **`/root`:**
  * ... (Achtung: Nicht verwechseln mit `/`. Das ist das Home-Verzeichnis für wen?)

---

## 🔐 User & Rechte Konzept
Linux ist ein Multi-User-System. Ich habe gelernt:

* **Root-User:** Der Administrator, der alles darf. (Vorsicht geboten!)
* **Sudo:** Ein Befehl, um kurzzeitig Root-Rechte zu bekommen ("SuperUser DO").
* **Chmod/Chown:** Befehle, um zu ändern, wem eine Datei gehört und wer sie lesen darf.

---

## 🛠 Praxis-Vorbereitung (To-Do für Zuhause)
- [ ] Backup meiner wichtigsten Daten erstellen
- [ ] Auf dem PC ca. 50-100 GB Speicher freimachen (Partition verkleinern)
- [ ] Ubuntu ISO Datei herunterladen
- [ ] USB-Stick mit Rufus/BalenaEtcher erstellen

---
*Notiz: Dieser Eintrag wurde mobil/am Laptop erstellt. Die praktische Installation folgt, sobald ich wieder an meinem Setup bin.*
