# Academic Performance Analyzer
---
## 📜 Project Overview:
- The project predicts students' academic performance (marks) based on the number of study hours per day. Using a Linear Regression model, the system establishes a correlation between study hours and marks, 
  providing accurate and realistic predictions. The project includes two user interfaces: one developed using Flask for web-based interaction and another using Streamlit for a modern, interactive dashboard. The 
  system also logs predictions and user inputs in a CSV file for further analysis.
---
## 📦 Dataset:
 - **Name:** Student Study Hours and Marks Dataset
 - **Features:**
   - `Study Hours:` Number of hours a student studies per day (independent variable).
   - `Marks:` Percentage of marks obtained by the student (dependent variable).
 - **Source:** Synthetic or public dataset used for simplicity.
 - **Size:** Contains several rows of `Study Hours` and `Marks` data points.
---
## ⚙ Algorithm:
 - **Model Used:** Linear Regression
   - Chosen because the problem involves predicting continuous numerical values (marks).
   - The relationship between study hours and marks is assumed to be linear.
 - Why Linear Regression?
   - Simple and interpretable.
   - Effective for modeling relationships between two continuous variables.
---
## 🤖 Technology:
 - Programming Language: `Python`
 - Libraries Used:
 - Modeling: `Scikit-learn`, `NumPy`, `Pandas`
 - Visualization: `Matplotlib`, `Seaborn`
 - Frontend Development:
      - `Flask`: For web application with HTML templates.
      - `Streamlit`: For a quick and interactive user interface.
   - `Joblib`: For saving and loading trained models.
   - `CSV Handling`: Pandas for data storage and retrieval.
   - `Deployment Tools`: Flask and Streamlit for separate user interaction interfaces.
---
## 🔍 Data Preprocessing:
 1. **Data Cleaning:** Ensured no null or missing values in the dataset.
 2. **Feature Selection:** Used Study Hours as the independent variable.
 3. **Splitting Dataset:**
  - Train-Test Split: Divided the dataset into training (80%) and testing (20%) sets.
 5. **Feature Scaling:** Not required for linear regression in this case.
---
## 📑 Model:
 1. Model Training:
  - Linear Regression from Scikit-learn.
  - Fitted using the training data (`X_train` and `y_train`).
 2. Evaluation Metrics:
  - R² Score: Indicates how well the model explains the variance in marks.
  - Mean Squared Error (MSE): Measures average squared difference between predicted and actual values.
  - Mean Absolute Error (MAE): Measures average absolute difference.
---
## 🌐 Frontend Implementations:
1. Flask:
  - A web-based application with form-based inputs.
  - Users input study hours, and the app predicts marks and displays them on the page.
  - Stores prediction history in a CSV file.
2. Streamlit:
  - A modern, interactive dashboard with input widgets.
  - Displays prediction history in a sidebar and allows CSV downloads. 
  - Includes a "Clear History" feature to reset the stored data.
---
## 📈 Result:
 - **Model Accuracy:** The model achieved an 𝑅2 score of 0.952, indicating that it explains 95.2% of the variance in the target variable.
 - **Mean Squared Error (MSE):** The Mean Squared Error is 1.044, reflecting the average squared difference between the predicted and actual marks. This low value demonstrates that the predictions are close 
   to the true values.
 - **Performance Summary:**
   - The Linear Regression model is highly effective for predicting students' marks based on their study hours.
   - The dual frontends (Flask and Streamlit) provide users with easy access to predictions and insights.
---
## 🎯 Conclusion:
 - The project successfully implements a predictive analytics solution using Linear Regression. The model's high 𝑅2 value and low MSE validate its performance and reliability. The dual frontend 
   implementations enhance accessibility and interactivity, making the system practical for both end-users and analysts.
   
This project can be extended by incorporating additional features, such as:
 - Exploring other machine learning models to further improve prediction accuracy.
 - Adding factors like sleep, study techniques, or prior academic records for more robust predictions.
