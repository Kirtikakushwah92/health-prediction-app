import streamlit as st

from database.db import SessionLocal
from database.models import Patient

st.title("🗑️ Delete Patient")

db = SessionLocal()

patient_id = st.number_input(
    "Enter Patient ID",
    min_value=1,
    step=1
)

if st.button("Delete"):

    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if patient:

        db.delete(patient)

        db.commit()

        st.success("Patient Deleted Successfully")

    else:

        st.error("Patient Not Found")