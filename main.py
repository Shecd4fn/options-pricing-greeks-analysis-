from src.black_scholes import black_scholes
from src.binomial_tree import binomial_tree
from src.monte_carlo import monte_carlo_asian
from src.greeks import calculate_greeks
from src.visualizations import plot_greeks

# Example usage
S = 100  # Underlying asset price
K = 100  # Strike price
T = 1    # Time to maturity in years
r = 0.05 # Risk-free interest rate
sigma = 0.2  # Volatility

# Black-Scholes pricing
print("Black-Scholes Call Option Price:", black_scholes(S, K, T, r, sigma, option_type='call'))

# Binomial tree pricing
print("Binomial Tree American Call Option Price:", binomial_tree(S, K, T, r, sigma, steps=100, option_type='call', american=True))

# Monte Carlo simulation for Asian option
print("Monte Carlo Asian Call Option Price:", monte_carlo_asian(S, K, T, r, sigma))

# Calculate and display Greeks
greeks = calculate_greeks(S, K, T, r, sigma, option_type='call')
print("Greeks:", greeks)

# Plot Greeks
plot_greeks(S, K, T, r, sigma, option_type='call')
