import numpy as np 
def monte_carlo_barrier_option(S, K, T, r, sigma, barrier, simulations=10000, time_steps=252, option_type='call', barrier_type='up-and-out'):
    """
    Pricer for barrier options using Monte Carlo simulation.

    Parameters:
    S : float : Current price of the underlying asset.
    K : float : Strike price of the option.
    T : float : Time to maturity (in years).
    r : float : Risk-free interest rate.
    sigma : float : Volatility of the underlying asset.
    barrier : float : Barrier level for the option.
    simulations : int : Number of simulated paths.
    time_steps : int : Number of time steps within each simulation.
    option_type : str : 'call' or 'put'.
    barrier_type : str : 'up-and-out', 'up-and-in', 'down-and-out', or 'down-and-in'.

    Returns:
    float : The price of the barrier option.
    """
    dt = T / time_steps  # Time increment for each step
    payoffs = []

    for _ in range(simulations):
        path = [S]
        barrier_crossed = False

        for _ in range(1, time_steps):
            z = np.random.normal()
            S_t = path[-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
            path.append(S_t)

            # Check if the barrier condition is met
            if (barrier_type == 'up-and-out' and S_t >= barrier) or (barrier_type == 'down-and-out' and S_t <= barrier):
                barrier_crossed = True
                break
            elif (barrier_type == 'up-and-in' and S_t >= barrier) or (barrier_type == 'down-and-in' and S_t <= barrier):
                barrier_crossed = True

        # Calculate the payoff if the option is valid
        if ((barrier_type in ['up-and-out', 'down-and-out'] and not barrier_crossed) or
            (barrier_type in ['up-and-in', 'down-and-in'] and barrier_crossed)):
            final_price = path[-1]
            if option_type == 'call':
                payoff = max(final_price - K, 0)
            elif option_type == 'put':
                payoff = max(K - final_price, 0)
            else:
                raise ValueError("option_type must be 'call' or 'put'")
            payoffs.append(payoff)

    # Discount the average payoff to present value
    option_price = np.exp(-r * T) * np.mean(payoffs)
    return option_price

# Example usage
barrier_call_price = monte_carlo_barrier_option(S, K, T, r, sigma, barrier=120, simulations=100000, option_type='call', barrier_type='up-and-out')
print(f"Barrier Call Option Price (Monte Carlo, Up-and-Out): {barrier_call_price:.2f}")
