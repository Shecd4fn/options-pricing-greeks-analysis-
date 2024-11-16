import numpy as np

def monte_carlo_asian_option(S, K, T, r, sigma, simulations=10000, time_steps=252, option_type='call'):
    """
    Pricer for Asian options using Monte Carlo simulation.

    Parameters:
    S : float : Current price of the underlying asset.
    K : float : Strike price of the option.
    T : float : Time to maturity (in years).
    r : float : Risk-free interest rate.
    sigma : float : Volatility of the underlying asset.
    simulations : int : Number of simulated paths.
    time_steps : int : Number of time steps within each simulation.
    option_type : str : 'call' or 'put'.

    Returns:
    float : The price of the Asian option.
    """
    dt = T / time_steps  # Time increment for each step
    payoffs = []

    for _ in range(simulations):
        path = [S]
        for _ in range(1, time_steps):
            z = np.random.normal()
            S_t = path[-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
            path.append(S_t)

        # Calculate the average price of the path
        avg_price = np.mean(path)

        # Calculate the payoff
        if option_type == 'call':
            payoff = max(avg_price - K, 0)
        elif option_type == 'put':
            payoff = max(K - avg_price, 0)
        else:
            raise ValueError("option_type must be 'call' or 'put'")

        payoffs.append(payoff)

    # Discount the average payoff to present value
    option_price = np.exp(-r * T) * np.mean(payoffs)
    return option_price

# Example usage
S = 100      # Current price of the underlying asset
K = 100      # Strike price
T = 1        # Time to maturity (1 year)
r = 0.05     # Risk-free interest rate (5%)
sigma = 0.2  # Volatility (20%)

asian_call_price = monte_carlo_asian_option(S, K, T, r, sigma, simulations=100000, option_type='call')
print(f"Asian Call Option Price (Monte Carlo): {asian_call_price:.2f}")
