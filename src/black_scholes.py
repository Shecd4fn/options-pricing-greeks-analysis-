from scipy.stats import norm
import numpy as np

def black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    Calcule le prix d'une option européenne (call ou put) en utilisant le modèle de Black-Scholes.

    Paramètres :
    S : float : Prix de l'actif sous-jacent
    K : float : Prix d'exercice de l'option
    T : float : Temps jusqu'à l'échéance (en années)
    r : float : Taux d'intérêt sans risque
    sigma : float : Volatilité de l'actif sous-jacent
    option_type : str : Type de l'option ('call' ou 'put')

    Retourne :
    float : Prix de l'option
    """
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return price

