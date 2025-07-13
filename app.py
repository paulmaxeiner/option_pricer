import streamlit as st
import pandas as pd
import numpy as np
from black_scholes import black_scholes_price

st.title("Option Pricer")
st.sidebar.title("Navigation")

model = st.selectbox("Model", ["Black-Scholes"])

options = ["call","put"]
option_type = st.radio("Option Type", options, index=0)


S = st.number_input("Current Stock Price (S)", value=100.0, min_value=0.0, step=1.0)

K = st.slider("Strike Price (K)", 1, 500, int(S), step=1)
T = st.slider("Time to Maturity (T, years)", value=1.0, min_value=0.01, max_value=10.0, step=0.01)
r = st.slider("Risk-Free Rate (r)", 0.0, 0.2, 0.05)
q = st.slider("Continuous Dividend Yield (q)", 0.0, 0.1, 0.05)
sigma = st.slider("Volatility (σ)", 0.01, 2.0, 0.2)


price = black_scholes_price(S, K, T, r, q, sigma, option_type)
st.subheader(f"Option Price: ${price:.2f}")