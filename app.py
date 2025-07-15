import streamlit as st
import pandas as pd
import numpy as np
from black_scholes import black_scholes_price

st.title("Option Pricer")
st.sidebar.title("Navigation")
st.sidebar.markdown("A simple option pricing tool using the Black-Scholes model.")

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

stock_range = np.linspace(S*0.5, S*2, 100)
option_values = [
    black_scholes_price(s, K, T, r, q, sigma, option_type)
    for s in stock_range
]
payoff_at_expiration = np.maximum(stock_range - K, 0) if option_type == 'call' else np.maximum(K - stock_range, 0)
profit_at_expiration = option_values - price

simulation_data = pd.DataFrame(
    {
        "Stock Price": stock_range,
        "Option Price": option_values,
        "Payoff at Expiration": payoff_at_expiration,
        "Profit at Expiration": profit_at_expiration
    }
)

st.header("Graphs")

st.line_chart(simulation_data, x="Stock Price")

tab1, tab2 = st.tabs(["Payoff at Expiration", "Option Price vs Stock Price"])

with tab1:
    st.line_chart(simulation_data, x="Stock Price", y="Payoff at Expiration")
with tab2:
    st.line_chart(simulation_data, x="Stock Price", y="Option Price")

