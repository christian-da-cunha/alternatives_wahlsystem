import streamlit as st
import matplotlib.pyplot as plt

# Titel und Beschreibung der App
st.title("Anders wählen")
st.write("Aternativer Stimmzettel")
st.write("Entwicklung und Analyse eines alternativen Wahlsystems unter Nutzung von Business Analytics")
st.write("---")
st.write("Erstellt von Christian Kaufmann")


# Eingabe des Alters
st.subheader("1. Persönliche Daten")
alter = st.selectbox("Bitte geben Sie Ihr Alter an:", ["keine Angabe"] + [str(i) for i in range(16, 116)])
if alter != "keine Angabe":
    st.success("Alter erfolgreich eingegeben.")
else:
    st.error("Bitte geben Sie Ihr Alter ein.")

# Frage zur bevorzugten Partei
st.subheader("2. Bevorzugte Partei")
parteien = ["keine Angabe", "ÖVP", "SPÖ", "FPÖ", "GRÜNE", "NEOS", "BIER", "MFG", "BGE", "LMP", "GAZA", "KPÖ", "KEINE"]
bevorzugte_partei = st.selectbox("2. Welche Partei würden Sie wählen, wenn heute Wahlen wären?", parteien)
if bevorzugte_partei != "keine Angabe":
    st.success("Bevorzugte Partei erfolgreich ausgewählt.")
else:
    st.warning("Bitte wählen Sie eine Partei oder 'keine Angabe'.")

# Frage zur Negativstimme
st.subheader("3. Abgelehnte Partei")
negativstimme = st.selectbox("3. Welche Partei würden Sie eine Stimme abziehen (Negativstimme)?", parteien)
if negativstimme != "keine Angabe":
    st.success("Negativstimme erfolgreich ausgewählt.")
else:
    st.warning("Bitte wählen Sie eine Partei oder 'keine Angabe'.")

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
columns = st.columns(len(parteien) - 1)  # -1, da "keine Angabe" keine Punkte bekommt
for i, partei in enumerate(parteien[1:]):  # Beginne bei der ersten echten Partei, nicht "keine Angabe"
    with columns[i]:
        punkte = st.number_input(f"{partei}", min_value=0, max_value=10, step=1, key=partei)
        punkte_verteilung.append(punkte)

# Summe der vergebenen Punkte berechnen
vergebene_punkte = sum(punkte_verteilung)

# Prüfung der Gesamtpunktzahl und entsprechende Meldung
if vergebene_punkte != 10:
    st.error(f"Die Gesamtpunktzahl muss genau 10 betragen. Aktuell vergeben: {vergebene_punkte} Punkte.")
else:
    st.success(f"Sie haben genau 10 Punkte korrekt vergeben!")

# Tortengrafik der Punkteverteilung
if vergebene_punkte == 10:
    # Filtere Parteien, Punkte und Farben, um nur die mit mehr als 0 Punkten anzuzeigen
    parteien_filtered = [partei for i, partei in enumerate(parteien[1:]) if punkte_verteilung[i] > 0]
    punkte_filtered = [punkte for punkte in punkte_verteilung if punkte > 0]
    farben_filtered = [farben[i] for i in range(len(punkte_verteilung)) if punkte_verteilung[i] > 0]

    # Erstellen der Tortengrafik
    fig, ax = plt.subplots()
    ax.pie(
        punkte_filtered, 
        labels=parteien_filtered, 
        colors=farben_filtered,
        autopct=lambda p: f'{int(p * sum(punkte_filtered) / 100)}' if p > 0 else '',
        startangle=90
    )
    ax.axis('equal')
    st.pyplot(fig)
