import streamlit as st
from database.db import engine
from database.models import Base

st.set_page_config(
    page_title="Health Prediction App",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Health Prediction Application")

st.sidebar.title("Navigation")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Create Patient",
        "View Patients",
        "Update Patient",
        "Delete Patient"
    ]
)

if menu == "Create Patient":
    st.write("Create Patient Page")

elif menu == "View Patients":
    st.write("View Patients Page")

elif menu == "Update Patient":
    st.write("Update Patient Page")

elif menu == "Delete Patient":
    st.write("Delete Patient Page")
    
Base.metadata.create_all(bind=engine)