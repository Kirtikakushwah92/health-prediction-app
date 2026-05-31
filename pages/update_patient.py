import streamlit as st

from database.db import SessionLocal
from database.models import Patient

st.title("✏️ Update Patient")

db = SessionLocal()

# Fetch all patients
patients = db.query(Patient).all()

if not patients:
    st.warning("No patients available.")
    st.stop()

# Dropdown
patient_options = {
    f"ID {p.id} - {p.full_name}": p.id
    for p in patients
}

selected_patient = st.selectbox(
    "Select Patient",
    list(patient_options.keys())
)

patient_id = patient_options[selected_patient]

patient = db.query(Patient).filter(
    Patient.id == patient_id
).first()

# Form
full_name = st.text_input(
    "Full Name",
    value=patient.full_name
)

email = st.text_input(
    "Email",
    value=patient.email
)

glucose = st.number_input(
    "Glucose",
    value=float(patient.glucose)
)

haemoglobin = st.number_input(
    "Haemoglobin",
    value=float(patient.haemoglobin)
)

cholesterol = st.number_input(
    "Cholesterol",
    value=float(patient.cholesterol)
)

remarks = st.text_area(
    "Remarks",
    value=patient.remarks if patient.remarks else ""
)

if st.button("Update Patient"):

    patient.full_name = full_name
    patient.email = email
    patient.glucose = glucose
    patient.haemoglobin = haemoglobin
    patient.cholesterol = cholesterol
    patient.remarks = remarks

    db.commit()

    st.success("✅ Patient Updated Successfully")