import streamlit as st
import pandas as pd
from model import train_model

# Charger le modèle
model = train_model()

st.title("🎓 Student Success Prediction")

st.write("Entrez les informations de l'étudiant :")

# Inputs utilisateur
age = st.slider("Age", 15, 40, 20)
study_hours = st.slider("Heures d'étude", 1, 10, 3)
note = st.slider("Note", 0, 20, 10)

# Bouton prédiction
if st.button("Prédire"):
    data = pd.DataFrame([[age, study_hours, note]],
                        columns=["age", "study_hours", "note"])
    
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("✅ L'étudiant va réussir")
    else:
        st.error("❌ L'étudiant va échouer")