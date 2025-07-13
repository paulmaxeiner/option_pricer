## Using Python 3.12.7 (Anaconda)

import math
from scipy.stats import norm
import pandas as pd
from pulp import *
import pulp as pl

'''
Variables
---------------------------------
S = stock price
K = strike price
T = time to expiration in years
r = risk-free interest rate (annualized)
sigma = volatility of the underlying stock (annualized)
q = continuous dividend yield (annualized, default 0.0)
option_type = 'call' or 'put' (European options only)
'''

def black_scholes_price(S, K, T, r, q, sigma, option_type='call'):
    ## calculate d1 and d2
    d1 = (math.log(S / K)+(r - q + (pow(sigma,2)/2)) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    ## Black-Scholes formula
    if option_type == 'call':
        price = S * math.exp(-q*T) * norm.cdf(d1) - K * math.exp(-r*T)*norm.cdf(d2)
    elif option_type == 'put':
        price = K * math.exp(-r*T) * norm.cdf(-d2) - S * math.exp(-q*T) * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be either 'call' or 'put'")
    return price

# Test case (should output ~19.944, with S=100, K=100, T=1, r=0.05, q=0.03, sigma=0.5, and a call option)
print(black_scholes_price(100, 100, 1, 0.05, 0.03, 0.5, 'call'))