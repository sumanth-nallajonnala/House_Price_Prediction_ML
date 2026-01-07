🏠 **House Price Prediction Using Ridge Regression **

📌 Project Overview
This project implements a linear regression model to predict house prices based on:
- Square Footage
- Number of Bedrooms
- Number of Bathrooms

The model is trained using the King County House Sales dataset and deployed using Gradio.

---

## Dataset
Source: King County House Sales Dataset  
File used:
- kc_house_data.csv (original)
- kc_house_data_cleaned.csv (after preprocessing)

---

## Preprocessing Steps
1. Selected relevant features (sqft_living, bedrooms, bathrooms, price)
2. Removed missing values
3. Removed extreme outliers
4. Saved cleaned dataset for training

---

## Model Used
- Ridge Regression (Linear Regression with Regularization)
- Feature Scaling using StandardScaler
- Log transformation applied to target variable

---

## Evaluation Metrics
- Mean Squared Error (MSE)
- R² Score

---

## Deployment
The trained model is deployed using Gradio, allowing users to input house details and receive predicted prices interactively.

---

## Tools & Technologies
- Python
- Pandas, NumPy
- Scikit-learn
- Google Colab
- Gradio

---

## How to Run
1. Upload dataset in Google Colab
2. Run notebook cells sequentially
3. Launch Gradio interface
4. Enter inputs to predict house price

---

## Author
Name: Sumanth Nallajonnala 
Course / Institution: SASTRA Deemed University
