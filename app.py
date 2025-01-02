import numpy as np
import pandas as pd
import joblib
import streamlit as st
import base64

# Set up page title and layout
st.set_page_config(page_title="Academic Performance Analyzer", page_icon="📚")

# Function to set background image and text color
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        color: white;
    }}
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {{
        color: white;
    }}
    .stApp .stMarkdown p {{
        color: white;
    }}
    .stButton button {{
        background-color: #0078D7;
        color: white;
        border-radius: 5px;
        border: none;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set the background image
set_background("background1.jpg")

# Load the pre-trained model
model = joblib.load(r"student_mark_predictor.pkl")

# File path for storing prediction history
csv_file = 'smp_data_from_app.csv'

# Load the existing data from CSV if it exists
def load_data():
    if pd.io.common.file_exists(csv_file):
        return pd.read_csv(csv_file)
    else:
        return pd.DataFrame(columns=['Study Hours', 'Predicted Marks'])

# Streamlit web app
def main():
    # Sidebar for instructions, prediction history, and additional info
    with st.sidebar:
        st.title('🔧 Features')
        st.header('📘 Instructions')
        st.write("""
            1. Enter the number of hours you study per day in the input box below.
            2. Press the **Predict** button to get your estimated marks.
            3. View your prediction and history on the main page.
        """)
        st.subheader('📝 Prediction History')
        df = load_data()
        if df.empty:
            st.write("No prediction history available.")
        else:
            st.write(df.style.set_properties(**{'text-align': 'center'}))
        st.write("---")
        
    # Main title with larger text
    st.title('📚 Academic Performance Analyzer')
    
    # Add custom CSS to adjust text styles
    st.markdown("""
        <style>
        .big-text {
            font-size: 30px !important;
            font-weight: bold;
            color: white;
        }
        .small-text {
            font-size: 20px !important;
            color: white;
        }
        .prediction-text {
            font-size: 18px !important;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # User input for study hours with enhanced design and bigger label text
    st.markdown('<p class="big-text">Enter the number of hours you study per day:</p>', unsafe_allow_html=True)
    study_hours = st.number_input('Enter the number of hours you study per day:', min_value=0, max_value=24, step=1, key="study_hours")
    
    # Display the current study hours input with a smaller header and white text
    st.markdown(f'<p class="small-text">You are studying for {study_hours} hours per day.</p>', unsafe_allow_html=True)
    
    # Validate the input and display an error if out of range
    if study_hours < 0 or study_hours > 24:
        st.error('⚠️ Please enter valid hours between 0 and 24.')
        return

    # Add prediction button with an emoji for creativity
    if st.button('📈 Predict'):
        # Prepare the input features
        input_features = np.array([study_hours]).reshape(1, -1)
        
        # Predict the output (marks) using the trained model
        predicted_marks = model.predict(input_features)[0].round(2)
        
        # Cap the predicted marks between 0 and 100
        predicted_marks = min(max(predicted_marks, 0), 100)
        
        # Display the prediction result with smaller font and white color
        st.markdown(f'<p class="prediction-text">Predicted Marks: {predicted_marks}%</p>', unsafe_allow_html=True)
        st.success(f'You will score **{predicted_marks}%** marks if you study **{int(study_hours)}** hours per day.')
        
        # Load existing prediction history and append new data
        df = load_data()
        new_data = pd.DataFrame({'Study Hours': [study_hours], 'Predicted Marks': [predicted_marks]})
        df = pd.concat([df, new_data], ignore_index=True)

        # Save the updated data to CSV
        df.to_csv(csv_file, index=False)
        
        # Provide a download button for the CSV file
        st.download_button(
            label="📥 Download Prediction History",
            data=df.to_csv(index=False),
            file_name='prediction_history.csv',
            mime='text/csv'
        )

    # Clear Prediction History Button
    if st.sidebar.button("Clear Prediction History"):
        # Clear the stored CSV file
        df = pd.DataFrame(columns=['Study Hours', 'Predicted Marks'])
        df.to_csv(csv_file, index=False)
        st.sidebar.success("Prediction history cleared.")

# Run the app
if __name__ == "__main__":
    main()
