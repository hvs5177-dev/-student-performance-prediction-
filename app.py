import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# Load trained model

model = load_model("student_marks_prediction_model.h5", compile=False)

st.title("Student Performance Prediction System")
st.write("Enter student details to predict performance")

age = st.number_input("Age", 10, 25, 18)
study_hours = st.number_input("Study Hours Per Day", 0.0, 12.0)
attendance = st.number_input("Attendance Percentage", 0.0, 100.0)

math = st.number_input("Math Score", 0.0, 100.0)
science = st.number_input("Science Score", 0.0, 100.0)
english = st.number_input("English Score", 0.0, 100.0)
previous = st.number_input("Previous Year Score", 0.0, 100.0)

predict_button = st.button("Predict Performance")

if predict_button:

```
input_data = np.array([[age, study_hours, attendance, math, science, english, previous]])
input_data = input_data.reshape(1, input_data.shape[1], 1)

prediction = model.predict(input_data)
predicted_marks = float(prediction[0][0])

lower = round(predicted_marks - 4)
upper = round(predicted_marks + 4)

# Academic rule
if math < 20 or science < 20 or english < 20:
    result = "FAIL"
    risk = "High Risk"

elif predicted_marks >= 40:
    result = "PASS"

    if predicted_marks >= 75:
        risk = "Low Risk"
    elif predicted_marks >= 50:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

else:
    result = "FAIL"
    risk = "High Risk"

st.subheader("Prediction Result")
st.write("Predicted Marks:", round(predicted_marks, 2))
st.write("Marks Range:", lower, "-", upper)
st.write("Prediction:", result)
st.write("Risk Level:", risk)

st.subheader("Performance Chart")

subjects = ["Math", "Science", "English", "Predicted"]
scores = [math, science, english, predicted_marks]

fig, ax = plt.subplots()
ax.bar(subjects, scores)

ax.set_ylabel("Marks")
ax.set_title("Student Performance Overview")

st.pyplot(fig)
```
