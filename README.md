# 🏠 House Price Prediction Using Ridge Regression

## 📌 Project Overview
This project focuses on building a **house price prediction system** using **Ridge Regression**, a regularized linear regression technique.  
The model predicts house prices based on three key features:

- Square Footage  
- Number of Bedrooms  
- Number of Bathrooms  

The project demonstrates a complete **machine learning pipeline**, including data preprocessing, exploratory analysis, model training, evaluation, and interactive prediction.

---

## 📂 Dataset
**Source:** King County House Sales Dataset  

**Files Used:**
- `kc_house_data.csv` – Original dataset  
- `kc_house_data_cleaned.csv` – Cleaned dataset after preprocessing  

The dataset contains real-world housing data with multiple numerical attributes related to residential properties.

---

## 🧹 Data Preprocessing
The following preprocessing steps were applied to improve data quality and model performance:

1. Selected relevant features:  
   - `sqft_living`  
   - `bedrooms`  
   - `bathrooms`  
   - `price`
2. Removed missing values  
3. Removed extreme outliers to reduce skewness  
4. Applied feature scaling using **StandardScaler**  
5. Saved the cleaned dataset for reproducibility  

---

## 📊 Exploratory Data Analysis
To better understand the dataset and feature relationships, the following visualizations were created:

- **House Price vs Square Footage**
- **Feature Correlation Heatmap**
- **Actual vs Predicted House Prices**

These plots help validate feature relevance and model effectiveness.

---

## 🤖 Model Used
- **Ridge Regression** (Linear Regression with L2 regularization)
- Helps reduce overfitting and improve generalization
- Suitable for numerical, feature-based prediction problems
- Log transformation applied to the target variable to handle skewness

---

## 📈 Model Evaluation
The model was evaluated using standard regression metrics:

- **Mean Squared Error (MSE)**
- **R² Score**

The results indicate that the model performs reliably on unseen test data.

---

## 🔍 Sample Prediction
```python
model.predict([[2000, 3, 2]])
This predicts the house price for a property with:
2000 square feet
3 bedrooms
2 bathrooms
```
## 🖥️ Deployment
The trained model is integrated with Gradio, enabling an interactive interface where users can:
Enter house details
Receive predicted house prices in real time
The interface was tested using Google Colab.

---

## 🛠 Tools & Technologies
Python
Pandas, NumPy
Scikit-learn
Matplotlib
Google Colab
Gradio

---

## ▶️ How to Run the Project
Open the notebook in Google Colab
Upload the dataset files
Run all cells sequentially
Explore visualizations and evaluation results
(Optional) Launch the Gradio interface for interactive predictions

---

## 🔮 Future Improvements
Add more predictive features (location, year built, condition)
Try Polynomial or ElasticNet Regression
Perform hyperparameter tuning
Deploy as a full web application

---

##👤 Author
Sumanth Nallajonnala
B.Tech – Information Technology
SASTRA Deemed University
