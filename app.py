import gradio as gr
import pandas as pd
import joblib

model = joblib.load("ridge_model.pkl")
scaler = joblib.load("scaler.pkl")

def predict_price(sqft, bedrooms, bathrooms):
    data = pd.DataFrame(
        [[sqft, bedrooms, bathrooms]],
        columns=["sqft", "bedrooms", "bathrooms"]
    )
    data_scaled = scaler.transform(data)
    prediction = model.predict(data_scaled)[0]
    return f"Predicted House Price: ₹{prediction:,.2f}"

interface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Square Footage"),
        gr.Number(label="Bedrooms"),
        gr.Number(label="Bathrooms")
    ],
    outputs="text",
    title="House Price Prediction",
    description="Ridge Regression model using sqft, bedrooms, and bathrooms"
)

interface.launch()
