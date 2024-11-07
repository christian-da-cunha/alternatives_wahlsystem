import streamlit as st
import matplotlib.pyplot as plt

# Titel und Beschreibung der App
st.title("Alternatives Wahlsystem - Punktevergabe")
st.write("Verteilen Sie genau 10 Punkte auf die Parteien nach Ihrem Ermessen. Die Gesamtpunktzahl muss 10 betragen.")

# Eingabe von Geburtsdatum und Postleitzahl
geburtsdatum = st.date_input("Bitte geben Sie Ihr Geburtsdatum ein:")
plz = st.text_input("Bitte geben Sie Ihre 4-stellige Postleitzahl ein:")

# Überprüfen, ob Postleitzahl 4-stellig ist
if not plz.isdigit() or len(plz) != 4:
    st.error("Die Postleitzahl muss 4-stellig sein.")
else:
    # Frage zur bevorzugten Partei
    bevorzugte_partei = st.selectbox(
        "Welche Partei würden Sie wählen, wenn heute Wahlen wären?",
        parteien
    )

    # Frage zur Negativstimme
    negativstimme = st.selectbox(
        "Welche Partei würden Sie eine Stimme abziehen (Negativstimme)?",
        parteien
    )

    # Parteienliste
    parteien = ["ÖVP", "SPÖ", "FPÖ", "GRÜNE", "NEOS", "BIER", "MFG", "BGE", "LMP", "GAZA", "KPÖ", "KEINE"]
    punkte_verteilung = []

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
