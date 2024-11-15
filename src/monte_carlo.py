def monte_carlo_asian(S, K, T, r, sigma, simulations=10000, option_type='call'):
    dt = T / 252  # Assume 252 trading days in a year
    payoff_sum = 0

    for _ in range(simulations):
        prices = [S]
        for _ in range(252):
            z = np.random.normal()
            prices.append(prices[-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z))
        avg_price = np.mean(prices)
        
        if option_type == 'call':
            payoff = max(0, avg_price - K)
        elif option_type == 'put':
            payoff = max(0, K - avg_price)
        payoff_sum += payoff

    price = (payoff_sum / simulations) * np.exp(-r * T)
    return price