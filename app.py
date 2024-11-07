import streamlit as st
import matplotlib.pyplot as plt

# Titel und Beschreibung der App
st.title("Alternatives Wahlsystem - Punktevergabe")
st.write("Verteilen Sie genau 10 Punkte auf die Parteien nach Ihrem Ermessen. Die Gesamtpunktzahl muss 10 betragen.")

# Eingabe des Alters
alter = st.number_input("1. Bitte geben Sie Ihr Alter ein:", min_value=16, max_value=115, step=1)
if alter:
    st.success("Alter erfolgreich eingegeben.")
else:
    st.warning("Bitte geben Sie Ihr Alter ein.")

# Frage zur bevorzugten Partei
parteien = ["ÖVP", "SPÖ", "FPÖ", "GRÜNE", "NEOS", "BIER", "MFG", "BGE", "LMP", "GAZA", "KPÖ", "KEINE"]
bevorzugte_partei = st.selectbox("2. Welche Partei würden Sie wählen, wenn heute Wahlen wären?", parteien)
if bevorzugte_partei:
    st.success("Bevorzugte Partei erfolgreich ausgewählt.")
else:
    st.warning("Bitte wählen Sie eine Partei.")

# Frage zur Negativstimme
negativstimme = st.selectbox("3. Welche Partei würden Sie eine Stimme abziehen (Negativstimme)?", parteien)
if negativstimme:
    st.success("Negativstimme erfolgreich ausgewählt.")
else:
    st.warning("Bitte wählen Sie eine Partei.")

# Überschrift für die Punktevergabe
st.subheader("4. Punktevergabe an die Parteien")

# Farbenliste für die Parteien
farben = [
    "#61c3ce",  # ÖVP - Türkis
    "#e02a12",  # SPÖ - Rot
    "#115093",  # FPÖ - Blau
    "#74a201",  # GRÜNE - Grün
    "#c21d62",  # NEOS - Pink
    "#ffea00",  # BIER - Gelb
    "#fe5826",  # MFG - Türkis
    "#fcfbe6",  # BGE - Hellblau
    "#4d194a",  # LMP - Orange
    "#a5dcb4",  # GAZA - Grau
    "#e70037",  # KPÖ - Dunkelrot
    "#ff9273"   # KEINE - Dunkelgrau
]

# Erstellen von Spalten für die Eingabefelder
punkte_verteilung = []
columns = st.columns(len(parteien))
for i, partei in enumerate(parteien):
    with columns[i]:  # Jede Partei in eine eigene Spalte setzen
        punkte = st.number_input(f"{partei}", min_value=0, max_value=10, step=1, key=partei)
        punkte_verteilung.append(punkte)

# Summe der vergebenen Punkte berechnen
vergebene_punkte = sum(punkte_verteilung)

# Prüfung der Gesamtpunkte und entsprechende Meldung (oberhalb der Eingabefelder)
if vergebene_punkte != 10:
    st.error(f"Die Gesamtpunktzahl muss genau 10 betragen. Aktuell vergeben: {vergebene_punkte} Punkte.")
else:
    st.success(f"Sie haben genau 10 Punkte korrekt vergeben!")

# Tortengrafik der Punkteverteilung
if vergebene_punkte == 10:
    # Filtere Parteien, Punkte und Farben, um nur die mit mehr als 0 Punkten anzuzeigen
    parteien_filtered = [partei for i, partei in enumerate(parteien) if punkte_verteilung[i] > 0]
    punkte_filtered = [punkte for punkte in punkte_verteilung if punkte > 0]
    farben_filtered = [farben[i] for i in range(len(punkte_verteilung)) if punkte_verteilung[i] > 0]

    # Erstellen der Tortengrafik
    fig, ax = plt.subplots()
    ax.pie(
        punkte_filtered, 
        labels=parteien_filtered, 
        colors=farben_filtered,  # Farben für die Parteien
        autopct=lambda p: f'{int(p * sum(punkte_filtered) / 100)}' if p > 0 else '', 
        startangle=90
    )
    ax.axis('equal')  # Gleichmäßige Darstellung der Torte
    st.pyplot(fig)
