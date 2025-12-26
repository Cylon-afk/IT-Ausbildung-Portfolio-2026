# 🐧 Woche 1: Linux Foundation & Installation

> **Status:** 🟡 In Arbeit (Theorie-Phase)
> **System:** Ubuntu 24.04 LTS (geplant für Dual-Boot)

## 🎯 Lernziele dieser Woche
- [x] Architektur von Linux verstehen (Kernel, Shell, User-Space)
- [x] Das Dateisystem (File System Hierarchy) kennenlernen
- [ ] Vorbereitung der Installation (Partitionierung)

---

## 📚 Theorie-Journal (Heute gelernt)

Bevor ich das System installiere, habe ich mich mit der Struktur von Linux befasst. Anders als bei Windows (Laufwerk C:\) gibt es bei Linux einen einzigen Verzeichnisbaum, der bei `/` (Root) beginnt.

### 📂 Das Dateisystem erklärt (FHS - Filesystem Hierarchy Standard)
Meine Recherche zu den wichtigsten System-Ordnern:

* **`/` (Root Verzeichnis):**
  * Der Startpunkt des gesamten Systems. Alle anderen Ordner und Laufwerke sind hier eingehängt. Vergleichbar mit "Dieser PC", aber ohne Buchstaben.

* **`/home`:**
  * Hier liegen die persönlichen Daten der Benutzer (z. B. `/home/cylon/Dokumente`). Das ist der einzige Ort, an dem normale User volle Schreibrechte haben (Sandbox-Prinzip).

* **`/etc`:**
  * Enthält die systemweiten Konfigurationsdateien. Hier wird eingestellt, wie das Netzwerk, der Bootvorgang oder User-Rechte funktionieren. (Merksatz: "Editable Text Configuration").

* **`/var`:**
  * Steht für "Variable". Hier liegen Dateien, die sich ständig ändern, wie z. B. System-Logs (`/var/log`) oder Webserver-Dateien (`/var/www`). Wichtig für Forensik und Fehlersuche!

* **`/bin` & `/usr/bin`:**
  * Hier liegen die ausführbaren Programme (Binaries) für alle User, wie z. B. `ls`, `cp`, `python` oder `nano`.

* **`/root`:**
  * Achtung: Nicht verwechseln mit `/`. Dies ist das spezielle Home-Verzeichnis **nur für den Administrator (Root)**. Normale User haben hier keinen Zutritt.

---

## 🔐 User & Rechte Konzept (Permissions)
Linux trennt strikt zwischen Administrator und Nutzer, um Sicherheit zu gewährleisten.

* **Root-User (UID 0):**
  * Der Super-Admin. Hat Zugriff auf jede Datei und kann jeden Prozess beenden. Sollte nie für die tägliche Arbeit genutzt werden (Sicherheitsrisiko).
  
* **Standard User:**
  * Kann Programme nutzen und Dateien im eigenen Home-Ordner bearbeiten. Kann das System selbst nicht beschädigen.

* **Sudo (SuperUser DO):**
  * Ein Mechanismus, der es berechtigten Standard-Usern erlaubt, **temporär** Root-Rechte für einen einzelnen Befehl zu erhalten. Das ist der Goldstandard für sicheres Arbeiten.

---

## 🛠 Praxis-Vorbereitung (To-Do für Zuhause)
- [ ] Backup meiner wichtigsten Daten erstellen
- [ ] Auf dem PC ca. 50-100 GB Speicher freimachen (Partition verkleinern)
- [ ] Ubuntu ISO Datei herunterladen
- [ ] USB-Stick mit Rufus/BalenaEtcher erstellen

---
*Notiz: Dieser Eintrag wurde mobil erstellt. Die praktische Installation folgt, sobald ich wieder an meinem Setup bin.*
---
*Notiz: Dieser Eintrag wurde mobil/am Laptop erstellt. Die praktische Installation folgt, sobald ich wieder an meinem Setup bin.*
