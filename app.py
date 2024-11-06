import streamlit as st
import matplotlib.pyplot as plt

# Titel und Beschreibung der App
st.title("Alternatives Wahlsystem - Punktevergabe")
st.write("Verteilen Sie genau 10 Punkte auf die Parteien nach Ihrem Ermessen. Die Gesamtpunktzahl muss 10 betragen.")

# CSS für Styling
st.markdown(
    """
    <style>
    .number-input {
        width: 100px !important; /* Schmale Breite */
        height: 60px !important; /* Größere Höhe */
        font-size: 24px !important; /* Größere Schriftgröße */
        text-align: center; /* Zentrierte Zahl */
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Parteienliste
parteien = ["ÖVP", "SPÖ", "FPÖ", "GRÜNE", "NEOS", "BIER", "MFG", "BGE", "LMP", "GAZA", "KPÖ", "KEINE"]
punkte_verteilung = []

# Punktevergabe mit gestylten Eingabefeldern
for partei in parteien:
    punkte = st.number_input(
        f"Punkte für {partei}:",
        min_value=0,
        max_value=10,
        step=1,
        key=partei,
        format="%d"
    )
    # Hinzufügen von CSS-Klassen für die Eingabefelder
    st.markdown(f'<div class="number-input"></div>', unsafe_allow_html=True)
    punkte_verteilung.append(punkte)

# Summe der vergebenen Punkte berechnen
vergebene_punkte = sum(punkte_verteilung)

# Prüfung der Gesamtpunkte und entsprechende Meldung
if vergebene_punkte != 10:
    st.error(f"Die Gesamtpunktzahl muss genau 10 betragen. Aktuell vergeben: {vergebene_punkte} Punkte.")
else:
    st.success(f"Sie haben genau 10 Punkte korrekt vergeben!")

# Ausgabe der Punkteverteilung
st.write("Ihre Punkteverteilung:")
for i, partei in enumerate(parteien):
    st.write(f"{partei}: {punkte_verteilung[i]} Punkte")

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
