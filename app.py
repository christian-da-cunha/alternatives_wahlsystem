import streamlit as st

# Titel und Beschreibung der App
st.title("Alternatives Wahlsystem - Punktevergabe")
st.write("Verteilen Sie genau 10 Punkte auf die Parteien nach Ihrem Ermessen. Die Gesamtpunktzahl muss 10 betragen.")

# Korrigierte Parteienliste
parteien = ["ÖVP", "SPÖ", "FPÖ", "GRÜNE", "NEOS", "BIER", "MFG", "BGE", "LMP", "GAZA", "KPÖ", "KEINE"]
punkte_verteilung = []

# Punktevergabe mit Dropdowns
for partei in parteien:
    punkte = st.number_input(f"Punkte für {partei}:", min_value=0, max_value=10, step=1, key=partei)
    punkte_verteilung.append(punkte)

# Prüfung der Gesamtpunkte
if sum(punkte_verteilung) != 10:
    st.error("Die Gesamtpunktzahl muss genau 10 betragen. Bitte passen Sie die Punkteverteilung an.")
else:
    st.success("Sie haben genau 10 Punkte korrekt vergeben!")

# Ausgabe der Punkteverteilung
st.write("Ihre Punkteverteilung:")
for i, partei in enumerate(parteien):
    st.write(f"{partei}: {punkte_verteilung[i]} Punkte")

# Hier können Sie weitere Analysen oder Visualisierungen hinzufügen
