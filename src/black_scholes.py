
def binomial_tree(S, K, T, r, sigma, steps=100, option_type='call', american=False):
    dt = T / steps
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    # Initialize asset price tree
    asset_prices = np.zeros((steps + 1, steps + 1))
    for i in range(steps + 1):
        for j in range(i + 1):
            asset_prices[j, i] = S * (u**j) * (d**(i - j))

    # Initialize option price tree
    option_prices = np.zeros_like(asset_prices)
    if option_type == 'call':
        option_prices[:, -1] = np.maximum(0, asset_prices[:, -1] - K)
    elif option_type == 'put':
        option_prices[:, -1] = np.maximum(0, K - asset_prices[:, -1])

    # Backward induction
    for i in range(steps - 1, -1, -1):
        for j in range(i + 1):
            option_prices[j, i] = np.exp(-r * dt) * (p * option_prices[j + 1, i + 1] + (1 - p) * option_prices[j, i + 1])
            if american:
                option_prices[j, i] = max(option_prices[j, i], (asset_prices[j, i] - K) if option_type == 'call' else (K - asset_prices[j, i]))

    return option_prices[0, 0]
