import streamlit as st
import numpy as np
import joblib

model = joblib.load('sonar_model.sav')

st.title("🔍 SONAR Rock vs Mine Prediction")
st.write("Paste all 60 comma-separated values below:")

# Text area to paste input
input_str = st.text_area("Enter 60 comma-separated values")

if st.button("Predict"):
    try:
        input_list = [float(x.strip()) for x in input_str.split(",")]
        
        if len(input_list) != 60:
            st.error("❌ Please enter exactly 60 numbers.")
        else:
            input_data = np.array(input_list).reshape(1, -1)
            prediction = model.predict(input_data)

            if prediction[0] == 'R':
                st.success("✅ The object is a **Rock** 🪨")
            else:
                st.error("⚠️ The object is a **Mine** 💣")
    except:
        st.error("❌ Invalid input. Please enter only numbers, separated by commas.")
