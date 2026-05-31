import streamlit as st
from services.ai_service import generate_health_prediction
from database.db import SessionLocal
from database.models import Patient
from datetime import date
from services.validation import (
    validate_email,
    validate_dob
)

st.title("➕ Create Patient")

full_name = st.text_input("Full Name")

dob = st.date_input("Date of Birth",
                        value=date(2000, 1, 1),
                        min_value=date(1900, 1, 1),
                        max_value=date.today()
                    )

email = st.text_input("Email Address")

glucose = st.number_input(
    "Glucose",
    min_value=0.0
)

haemoglobin = st.number_input(
    "Haemoglobin",
    min_value=0.0
)

cholesterol = st.number_input(
    "Cholesterol",
    min_value=0.0
)

if st.button("Save Patient"):

    if not validate_email(email):
        st.error("Invalid Email Address")

    elif not validate_dob(dob):
        st.error("Date of Birth cannot be in future")

    else:

        db = SessionLocal()

        patient = Patient(
            full_name=full_name,
            dob=str(dob),
            email=email,
            glucose=glucose,
            haemoglobin=haemoglobin,
            cholesterol=cholesterol,
            remarks = generate_health_prediction(
                    glucose,
                    haemoglobin,
                    cholesterol
            )
        )

        db.add(patient)
        db.commit()

        st.success("Patient Saved Successfully")