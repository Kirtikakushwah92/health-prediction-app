import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_health_prediction(
    glucose,
    haemoglobin,
    cholesterol
):

    prompt = f"""
    You are a healthcare AI assistant.

    Analyze the following blood test values:

    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Predict possible health risks.

    Give a short response in 2-3 lines.
    """

    response = model.generate_content(prompt)

    return response.text