import streamlit as st
from streamlit_lottie import st_lottie
import numpy as np
import pickle
import json
import pathlib
import pygame
pygame.init()

model = pickle.load(open("gold.pkl", "rb"))

def css_file(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

filepath = pathlib.Path("gold.css")
css_file(filepath)

def load_lottie_file(filepath: str):
    with open(filepath, "rb") as f:
        return json.load(f)
data_gold = load_lottie_file("gold.json")
data_coin = load_lottie_file("Coin_purse.json")

st.markdown("""
<h1 style="color:black;text-align:center;background-color:#4CAF50;border-radius:10px">
💰 Gold Price Prediction App</h1>
""",unsafe_allow_html=True)

st.markdown("""
<h6 style="color:white;text-align:left;margin-top:20px;border-bottom:1px solid white;width:55%;">
Enter the values below to predict Gold Price (GLD):</h6>
""",unsafe_allow_html=True)

spx = st.number_input("**SPX Index Value**")
uso = st.number_input("**USO (Oil Fund)**")
slv = st.number_input("**SLV (Silver ETF)**")
eurusd = st.number_input("**EUR/USD Exchange Rate**")

if st.button("**Predict**",key="predict"):
    pygame.mixer.music.load("coin_1.wav")
    pygame.mixer.music.play()
    features = np.array([[spx, uso, slv, eurusd]])
    prediction = model.predict(features)
    st.subheader(f"Predicted Gold Price (GLD): {prediction[0]:.2f}")

st_lottie(data_coin, height=250, width=None)

with st.sidebar:
    st.markdown("""
    # 📘 About this Project
    ---
    This web app predicts the **Gold Price (GLD)** based on key financial indicators:
    - **SPX** – S&P 500 Index  
    - **USO** – United States Oil Fund (Crude Oil)  
    - **SLV** – Silver ETF Price  
    - **EUR/USD** – Euro to US Dollar exchange rate  
 
    You can enter new financial values below to see the **predicted gold price** instantly.

    """)
    st_lottie(data_gold, height=300, width=None)