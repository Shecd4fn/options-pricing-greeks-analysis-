import numpy as np
from black_scholes import black_scholes

def calculate_greeks(S, K, T, r, sigma, option_type='call'):
    delta_S = 1e-4 * S
    price_base = black_scholes(S, K, T, r, sigma, option_type)
    
    # Delta
    price_up = black_scholes(S + delta_S, K, T, r, sigma, option_type)
    delta = (price_up - price_base) / delta_S

    # Gamma
    price_down = black_scholes(S - delta_S, K, T, r, sigma, option_type)
    gamma = (price_up - 2 * price_base + price_down) / (delta_S ** 2)

    # Vega
    delta_sigma = 1e-4
    price_vega = black_scholes(S, K, T, r, sigma + delta_sigma, option_type)
    vega = (price_vega - price_base) / delta_sigma

    # Theta
    delta_T = 1 / 365
    price_theta = black_scholes(S, K, T - delta_T, r, sigma, option_type)
    theta = (price_theta - price_base) / delta_T

    # Rho
    delta_r = 1e-4
    price_rho = black_scholes(S, K, T, r + delta_r, sigma, option_type)
    rho = (price_rho - price_base) / delta_r

    return {'Delta': delta, 'Gamma': gamma, 'Vega': vega, 'Theta': theta, 'Rho': rho}
