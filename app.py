import streamlit as st
import matplotlib.pyplot as plt

# Titel und Beschreibung der App
st.title("Alternatives Wahlsystem - Punktevergabe")
st.write("Verteilen Sie genau 10 Punkte auf die Parteien nach Ihrem Ermessen. Die Gesamtpunktzahl muss 10 betragen.")

# Parteienliste
parteien = ["ÖVP", "SPÖ", "FPÖ", "GRÜNE", "NEOS", "BIER", "MFG", "BGE", "LMP", "GAZA", "KPÖ", "KEINE"]
punkte_verteilung = []

# Punktevergabe mit Dropdowns
for partei in parteien:
    punkte = st.number_input(f"Punkte für {partei}:", min_value=0, max_value=10, step=1, key=partei)
    punkte_verteilung.append(punkte)

# Summe der vergebenen Punkte berechnen
vergebene_punkte = sum(punkte_verteilung)

# Prüfung der Gesamtpunkte und entsprechende Meldung (oberhalb der Eingabefelder)
if vergebene_punkte != 10:
    st.error(f"Die Gesamtpunktzahl muss genau 10 betragen. Aktuell vergeben: {vergebene_punkte} Punkte.")
else:
    st.success(f"Sie haben genau 10 Punkte korrekt vergeben!")

# Ausgabe der Punkteverteilung
st.write("Ihre Punkteverteilung:")
for i, partei in enumerate(parteien):
    st.write(f"{partei}: {punkte_verteilung[i]} Punkte")

# Prüfung der Gesamtpunkte und entsprechende Meldung (unterhalb der Eingabefelder)
if vergebene_punkte != 10:
    st.error(f"Die Gesamtpunktzahl muss genau 10 betragen. Aktuell vergeben: {vergebene_punkte} Punkte.")
else:
    st.success(f"Sie haben genau 10 Punkte korrekt vergeben!")

# Tortengrafik der Punkteverteilung
if vergebene_punkte == 10:
    # Filtere Parteien und Punkte, um nur die mit mehr als 0 Punkten anzuzeigen
    parteien_filtered = [partei for i, partei in enumerate(parteien) if punkte_verteilung[i] > 0]
    punkte_filtered = [punkte for punkte in punkte_verteilung if punkte > 0]

    # Erstellen der Tortengrafik
    fig, ax = plt.subplots()
    ax.pie(
        punkte_filtered, 
        labels=parteien_filtered, 
        autopct=lambda p: f'{int(p * sum(punkte_filtered) / 100)} Punkte' if p > 0 else '', 
        startangle=90
    )
    ax.axis('equal')  # Gleichmäßige Darstellung der Torte
    st.pyplot(fig)
