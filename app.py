import streamlit as st
import pickle
import numpy as np

# Load saved model
model = pickle.load(open("student_purchase_model.pkl", "rb"))

st.title("🎓 Student Course Purchase Prediction")

st.write("Enter student details to predict purchase behavior")

# Input fields
age = st.number_input("Age", min_value=10, max_value=60)
study_hours = st.number_input("Study Hours per Week", min_value=0, max_value=60)
courses_completed = st.number_input("Previous Courses Completed", min_value=0, max_value=50)
platform_visits = st.number_input("Platform Visits per Month", min_value=0, max_value=200)
assignment_rate = st.slider("Assignment Completion Rate (%)", 0, 100)

# Predict button
if st.button("Predict"):
    input_data = np.array([[age, study_hours, courses_completed, platform_visits, assignment_rate]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Student Likely to Purchase Course")
    else:
        st.error("❌ Student Not Likely to Purchase Course")