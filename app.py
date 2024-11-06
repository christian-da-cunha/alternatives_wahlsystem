import streamlit as st

# Titel und Beschreibung der App
st.title("Alternatives Wahlsystem - Punktevergabe")
st.write("Verteilen Sie 10 Punkte auf die Parteien nach Ihrem Ermessen.")

# Parteienliste
parteien = ["Partei A", "Partei B", "Partei C", "Partei D"]
punkte_verteilung = []

# Punktevergabe
for partei in parteien:
    punkte = st.slider(f"{partei}:", 0, 10, 0)
    punkte_verteilung.append(punkte)

# Prüfung der Gesamtpunkte
if sum(punkte_verteilung) > 10:
    st.error("Die Gesamtpunktzahl darf nicht mehr als 10 betragen.")
else:
    st.success(f"Sie haben insgesamt {sum(punkte_verteilung)} Punkte vergeben.")

# Ausgabe der Punkteverteilung
st.write("Ihre Punkteverteilung:")
for i, partei in enumerate(parteien):
    st.write(f"{partei}: {punkte_verteilung[i]} Punkte")

# Hier können Sie weitere Analysen oder Visualisierungen hinzufügen
