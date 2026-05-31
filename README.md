# Health Prediction Application

## Overview

Health Prediction Application is a Streamlit-based web application that allows users to manage patient health records and generate AI-powered health risk predictions based on blood test values.

The application supports CRUD operations, data validation, persistent storage using SQLite, and AI integration using the Gemini API.

---

## Features

### Patient Management

* Create Patient Records
* View Patient Records
* Update Patient Records
* Delete Patient Records

### Data Validation

* Email format validation
* Date of Birth validation
* Numeric validation for blood test values

### Health Prediction

* Gemini AI Integration
* Generates health risk analysis based on:

  * Glucose
  * Haemoglobin
  * Cholesterol

### Database

* SQLite Database
* Persistent patient storage

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* SQLite
* SQLAlchemy ORM

### AI Service

* Google Gemini API

---

## Project Structure

health-prediction-app/

├── app.py

├── database/

│ ├── db.py

│ └── models.py

├── pages/

│ ├── create_patient.py

│ ├── view_patients.py

│ ├── update_patient.py

│ └── delete_patient.py

├── services/

│ ├── ai_service.py

│ └── validation.py

├── requirements.txt

├── README.md

└── .gitignore

---

## Installation

### Clone Repository

git clone YOUR_GITHUB_REPOSITORY_URL

cd health-prediction-app

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Application

streamlit run app.py

---

## AI Prediction Workflow

1. User enters patient information.
2. Blood test values are validated.
3. Gemini API processes the blood values.
4. Health risk prediction is generated.
5. Prediction is stored in the Remarks field.
6. Record is saved into SQLite database.

---

## Future Enhancements

* Patient Search
* CSV Export
* Authentication System
* Advanced Health Risk Prediction Models
* Dashboard Analytics

---

## Author

Kirtika Kushwah
B.Tech Computer Science Graduate
