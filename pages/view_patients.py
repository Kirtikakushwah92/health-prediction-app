import streamlit as st
import pandas as pd

from database.db import SessionLocal
from database.models import Patient

st.title("📋 View Patients")

db = SessionLocal()

patients = db.query(Patient).all()

data = []

for patient in patients:

    data.append({
        "ID": patient.id,
        "Name": patient.full_name,
        "DOB": patient.dob,
        "Email": patient.email,
        "Glucose": patient.glucose,
        "Haemoglobin": patient.haemoglobin,
        "Cholesterol": patient.cholesterol,
        "Remarks": patient.remarks
    })

st.dataframe(pd.DataFrame(data))