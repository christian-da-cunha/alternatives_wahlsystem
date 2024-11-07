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
max_punkte = 10 if selected_partei == "Keine Angabe" else 10  # Maximal mögliche Punkte

# Schleife durch Parteien (ohne "Keine Angabe")
for i, partei in enumerate(pars
