# options-pricing-greeks-analysis

## Overview
This project provides Python implementations for pricing European, American, and exotic options and analyzing their Greeks (Delta, Gamma, Vega, Theta, Rho). The project uses the Black-Scholes model, binomial/trinomial trees, and Monte Carlo simulations for comprehensive options analysis.

## Project Structure
- **main.py**: Entry point for running the code.
- **src/**: Contains modules for various models and analyses.
- **data/**: (Optional) Sample data for testing.
- **notebooks/**: Jupyter notebooks for interactive analysis and visualization.

## Features
- Implementation of the Black-Scholes model for European options.
- Binomial/trinomial tree pricing for American options.
- Monte Carlo simulation for exotic options (e.g., Asian, barrier).
- Calculation and visualization of Greeks.

## Installation
1. Clone the repository:


## Mathematical Overview of the Binomial Tree Model

### 1. Introduction to the Binomial Tree Model
The binomial tree model is a numerical method used for pricing European and American options by simulating the possible future price paths of the underlying asset over discrete time intervals. It provides a flexible framework that can account for early exercise, making it especially useful for American options.

### 2. Asset Price Evolution
The model assumes that, at each time step, the underlying asset price can move either **up** or **down** by specific factors:
- **Up factor (u)**: The factor by which the asset price increases at each step.
- **Down factor (d)**: The factor by which the asset price decreases, defined as \( d = 1 / u \).

These factors are defined as:
- Up factor: \( u = exp(\sigma \times \sqrt{\Delta t}) \)
- Down factor: \( d = exp(-\sigma \times \sqrt{\Delta t}) \)

Where:
- \( \sigma \) is the volatility of the underlying asset.
- \( \Delta t = T / N \) is the time increment per step, with \( T \) being the total time to maturity and \( N \) the number of steps.
![Equation](.png)

### 3. Risk-Neutral Probability
To ensure that the option is priced in a risk-neutral framework, the model uses the risk-neutral probability \( p \), defined as:
\[
p = \frac{e^{r \Delta t} - d}{u - d}
\]

Where:
- **\( r \)**: Risk-free interest rate.

This ensures that the expected return on the underlying asset matches the risk-free rate.

### 4. Payoff Calculation at Maturity
At the final time step (maturity), the option payoff is calculated for each node:
- **Call option payoff**:
\[
\text{Payoff} = \max(S_T - K, 0)
\]
- **Put option payoff**:
\[
\text{Payoff} = \max(K - S_T, 0)
\]

Where:
- **\( S_T \)**: Asset price at maturity.
- **\( K \)**: Strike price of the option.

### 5. Backward Induction for Option Valuation
The option price at earlier nodes is calculated using backward induction:
\[
V_{i,j} = e^{-r \Delta t} [p \cdot V_{i+1, j+1} + (1 - p) \cdot V_{i+1, j}]
\]

For **American options**, the model checks for the possibility of early exercise:
- **American call option**:
\[
V_{i,j} = \max(S_{i,j} - K, e^{-r \Delta t} [p \cdot V_{i+1, j+1} + (1 - p) \cdot V_{i+1, j}])
\]
- **American put option**:
\[
V_{i,j} = \max(K - S_{i,j}, e^{-r \Delta t} [p \cdot V_{i+1, j+1} + (1 - p) \cdot V_{i+1, j}])
\]

### 6. Final Option Price
The option price at the root of the tree (node \( V_{0,0} \)) represents the present value of the option.

### 7. Advantages of the Binomial Tree Model
- **Flexibility**: Can handle American options and options with complex features.
- **Accuracy**: By increasing the number of steps, the model's output converges to the actual option price.
- **Applicability**: Suitable for modeling path-dependent options with modifications.

### 8. Comparison with Other Models
- **Black-Scholes Model**: Provides an analytical solution but is limited to European options.
- **Monte Carlo Simulation**: Useful for complex, path-dependent options but can be computationally intensive for early exercise features.

### Mathematical Intuition
The binomial tree model approximates the continuous-time stochastic process (Geometric Brownian Motion) of the underlying asset using discrete steps. It builds a tree of possible future outcomes and works backward to find the present value of the option by considering the risk-neutral expected payoff at each step.

