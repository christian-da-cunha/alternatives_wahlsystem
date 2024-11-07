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
parteien = ["Keine Angabe", "ÖVP", "SPÖ", "FPÖ", "GRÜNE", "NEOS", "BIER", "MFG", "BGE", "LMP", "GAZA", "KPÖ", "KEINE"]
selected_partei = st.radio("Welche Partei würden Sie wählen, wenn heute Wahlen wären?", parteien, index=0)

if selected_partei == "Keine Angabe":
    st.error("Bitte wählen Sie eine Partei.")
else:
    st.success(f"Bevorzugte Partei: {selected_partei}")

# Frage zur Negativstimme
st.subheader("3. Abgelehnte Partei")
negativ_partei = st.radio(
    "Welche Partei würden Sie eine Stimme abziehen (Negativstimme)?",
    parteien,
    index=0
)

if negativ_partei == "Keine Angabe":
    st.error("Bitte wählen Sie eine Partei.")
elif negativ_partei == selected_partei:
    st.error("Die abgelehnte Partei darf nicht mit der bevorzugten Partei übereinstimmen.")
else:
    st.success(f"Negativstimme: {negativ_partei}")

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
columns = st.columns(len(parteien) - 1)  # -1, da "Keine Angabe" keine Punkte bekommt
max_punkte_fuer_partei = 0

# Schleife durch Parteien (ohne "Keine Angabe")
for i, partei in enumerate(parteien[1:]):  # Beginne bei der ersten echten Partei
    with columns[i]:
        punkte = st.number_input(f"{partei}", min_value=0, max_value=10, step=1, key=partei)
        punkte_verteilung.append((partei, punkte))

# Summe der vergebenen Punkte berechnen
vergebene_punkte = sum(punkte for _, punkte in punkte_verteilung)

# Fehlerüberprüfung für die Punktevergabe
fehler = False

# 1. Überprüfung: Punkte für die abgelehnte Partei
for partei, punkte in punkte_verteilung:
    if partei == negativ_partei and punkte > 0:
        st.error(f"Der Partei '{negativ_partei}' dürfen keine Punkte zugewiesen werden.")
        fehler = True

# 2. Überprüfung: Keine Partei darf mehr Punkte bekommen als die bevorzugte Partei
if selected_partei != "Keine Angabe":
    max_punkte_fuer_partei = next(punkte for partei, punkte in punkte_verteilung if partei == selected_partei)
    for partei, punkte in punkte_verteilung:
        if partei != selected_partei and punkte > max_punkte_fuer_partei:
            st.error(f"Die Partei '{partei}' darf nicht mehr Punkte bekommen als die bevorzugte Partei '{selected_partei}'.")
            fehler = True

# Prüfung der Gesamtpunktzahl und entsprechende Meldung
if not fehler:
    if vergebene_punkte != 10:
        st.error(f"Die Gesamtpunktzahl muss genau 10 betragen. Aktuell vergeben: {vergebene_punkte} Punkte.")
    else:
        st.success(f"Sie haben genau 10 Punkte korrekt vergeben!")

# Tortengrafik der Punkteverteilung
if vergebene_punkte == 10 and not fehler:
    # Filtere Parteien, Punkte und Farben, um nur die mit mehr als 0 Punkten anzuzeigen
    parteien_filtered = [partei for partei, punkte in punkte_verteilung if punkte > 0]
    punkte_filtered = [punkte for _, punkte in punkte_verteilung if punkte > 0]
    farben_filtered = [farben[i] for i in range(len(punkte_verteilung)) if punkte_verteilung[i][1] > 0]

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
