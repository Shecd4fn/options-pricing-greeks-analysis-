import matplotlib.pyplot as plt
import numpy as np
from greeks import calculate_greeks

def plot_greeks(S, K, T, r, sigma, option_type='call'):
    prices = np.linspace(S * 0.8, S * 1.2, 100)
    deltas, gammas, vegas, thetas, rhos = [], [], [], [], []

    for price in prices:
        greeks = calculate_greeks(price, K, T, r, sigma, option_type)
        deltas.append(greeks['Delta'])
        gammas.append(greeks['Gamma'])
        vegas.append(greeks['Vega'])
        thetas.append(greeks['Theta'])
        rhos.append(greeks['Rho'])

    plt.figure(figsize=(10, 6))
    plt.plot(prices, deltas, label='Delta')
    plt.plot(prices, gammas, label='Gamma')
    plt.plot(prices, vegas, label='Vega')
    plt.plot(prices, thetas, label='Theta')
    plt.plot(prices, rhos, label='Rho')
    plt.title('Greeks Analysis')
    plt.xlabel('Underlying Price')
    plt.ylabel('Greeks')
    plt.legend()
    plt.show()
