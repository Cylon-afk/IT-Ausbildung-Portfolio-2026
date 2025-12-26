import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Kriterium 1: Länge (mindestens 8 Zeichen)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Zu kurz (min. 8 Zeichen)")

    # Kriterium 2: Enthält Zahlen?
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Keine Zahlen enthalten")

    # Kriterium 3: Enthält Großbuchstaben?
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Keine Großbuchstaben")

    # Kriterium 4: Enthält Sonderzeichen?
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Keine Sonderzeichen")

    # Ergebnis berechnen
    print(f"\n--- Analyse für: '{password}' ---")
    if score == 4:
        print("✅ Ergebnis: Starkes Passwort!")
    elif score >= 2:
        print("⚠️ Ergebnis: Mittelmäßiges Passwort.")
    else:
        print("🚨 Ergebnis: Unsicheres Passwort!")

    # Feedback ausgeben (nur wenn Fehler da sind)
    for item in feedback:
        print(item)

# --- Hauptprogramm ---
user_input = input("Gib ein Passwort zum Testen ein: ")
check_password_strength(user_input)
