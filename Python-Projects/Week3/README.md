# 🐍 Projekt: Password Strength Checker

> **Status:** 🟡 Prototyp (Code Review ausstehend)
> **Tech:** Python 3, RegEx (Regular Expressions)

## 📝 Beschreibung
Ein Security-Tool, das die Komplexität von Passwörtern analysiert.
Anders als einfache Checker nutzt dieses Skript **Regular Expressions (`re`)**, um gezielt nach Zahlen, Sonderzeichen und Mustern zu suchen. Es berechnet einen "Security Score" und gibt dem Nutzer direktes Feedback.

## ⚙️ Features
- [x] Überprüfung der Mindestlänge (8 Zeichen)
- [x] Scan nach Zahlen & Sonderzeichen (via RegEx)
- [x] Scoring-System (Unsicher / Mittel / Stark)
- [ ] **Geplant:** Admin-Policies (Verbot von "123456", min. 12 Zeichen)

## 🚀 Nutzung
Das Skript wird direkt im Terminal ausgeführt:

```bash
python password_checker.py
