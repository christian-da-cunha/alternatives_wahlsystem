import streamlit as st
import pandas as pd
import os

# Titel und Beschreibung der App
st.title("Alternativer Stimmzettel")
st.subheader("Datenerhebung im Rahmen der Masterarbeit im Studiengang Business Analytics an der Technikum Wien Academy")
st.write("---")
st.write("DANKE für die Mitwirkung!")
st.write("---")

# Eingabe des Alters mit Optionsfeldern für Altersgruppen
st.subheader("1. Angaben zu meiner Altersgruppe:")
st.write("Bitte wählen Sie Ihre Altersgruppe:")

# Altersgruppen mit Optionbox
age_groups = ["Keine Angabe", "16-30", "31-50", "51-70", "71-90", ">90"]
selected_age_group = st.radio("Altersgruppe:", age_groups, index=0)

if selected_age_group == "Keine Angabe":
    st.error("Bitte wählen Sie eine Altersgruppe aus.")
else:
    st.success(f"Altersgruppe: {selected_age_group}")

# Neues 2. Geschlecht abfragen
st.subheader("2. Angaben zu meinem Geschlecht")
gender_options = ["Keine Angabe", "divers", "männlich", "weiblich"]
selected_gender = st.radio("Geschlecht:", gender_options, index=0)

if selected_gender == "Keine Angabe":
    st.error("Bitte wählen Sie Ihr Geschlecht aus.")
else:
    st.success(f"Geschlecht: {selected_gender}")

# Frage zur bevorzugten Partei (verschoben auf Punkt 3)
st.subheader("3. Ich würde meine Stimme folgender Partei geben:")
parteien = ["Keine Angabe", "ÖVP", "SPÖ", "FPÖ", "GRÜNE", "NEOS", "BIER", "MFG", "BGE", "LMP", "GAZA", "KPÖ", "KEINE"]
selected_partei = st.radio("Welcher Partei würden Sie Ihre Stimme geben?", parteien, index=0)

if selected_partei == "Keine Angabe":
    st.error("Bitte wählen Sie eine Partei.")
else:
    st.success(f"Bevorzugte Partei: {selected_partei}")

# Frage zur Negativstimme (verschoben auf Punkt 4)
st.subheader("4. Niemals würde ich meine Stimme folgender Partei geben:")
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

# Überschrift für die Punktevergabe (verschoben auf Punkt 5)
st.subheader("5. So würde ich meine Punkte verteilen:")

# Erstellen von Spalten für die Eingabefelder
punkte_verteilung = []
columns = st.columns(len(parteien) - 1)  # -1, da "Keine Angabe" keine Punkte bekommt

# Schleife durch Parteien (ohne "Keine Angabe")
for i, partei in enumerate(parteien[1:]):
    with columns[i]:
        punkte = st.number_input(f"{partei}", min_value=0, max_value=10, step=1, key=partei)
        punkte_verteilung.append((partei, punkte))

# Summe der vergebenen Punkte berechnen
vergebene_punkte = sum(punkte for _, punkte in punkte_verteilung)

# Fehlerüberprüfung für die Punktevergabe
fehler = False

# 1. Überprüfung: Punkte für die abgelehnte Partei
