import streamlit as st

# Titel und Beschreibung der App
st.title("Alternatives Wahlsystem - Punktevergabe")
st.write("Verteilen Sie genau 10 Punkte auf die Parteien, indem Sie die Kästchen ankreuzen.")

# Parteienliste
parteien = ["Partei A", "Partei B", "Partei C", "Partei D"]
punkte_verteilung = {partei: 0 for partei in parteien}

# Anzahl der verfügbaren Punkte
total_punkte = 10
punkte_vergeben = 0

# Punktevergabe mit Checkboxen
for partei in parteien:
    st.write(f"{partei}:")
    # Erstellen Sie 5 Checkboxen für jede Partei
    for i in range(5):
        if st.checkbox(f"Punkt {i + 1} für {partei}", key=f"{partei}_{i}"):
            punkte_verteilung[partei] += 1
            punkte_vergeben += 1

# Prüfung der Gesamtpunkte
if punkte_vergeben != total_punkte:
    st.error(f"Sie müssen genau {total_punkte} Punkte vergeben. Aktuell vergeben: {punkte_vergeben}.")
else:
    st.success(f"Sie haben genau {total_punkte} Punkte vergeben!")

# Ausgabe der Punkteverteilung
st.write("Ihre Punkteverteilung:")
for partei, punkte in punkte_verteilung.items():
    st.write(f"{partei}: {punkte} Punkte")

# Hier können Sie weitere Analysen oder Visualisierungen hinzufügen
