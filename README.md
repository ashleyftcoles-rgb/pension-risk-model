# Pension Projection & Risk Model

A Python-based pension modelling project exploring how contributions, investment returns, inflation and investment uncertainty affect long-term retirement outcomes.

The project combines deterministic pension projections, sensitivity analysis and Monte Carlo simulation to move beyond a single pension estimate and quantify the uncertainty surrounding future retirement wealth.

## Project Overview

Long-term pension outcomes depend heavily on assumptions about investment performance, inflation and contribution levels. Small changes in these assumptions can have a substantial effect when compounded over several decades.

This project was developed to investigate three main questions:

- How do investment returns and contribution growth affect projected pension wealth?
- How does uncertainty in annual investment returns affect the distribution of retirement outcomes?
- What is the probability of achieving a specified real pension target under different investment assumptions?

The model progresses from a deterministic pension projection to a 10,000-simulation Monte Carlo model and sensitivity analysis.

## Model Assumptions

The baseline model uses the following assumptions:

| Parameter | Baseline Assumption |
|---|---:|
| Starting age | 21 |
| Retirement age | 66 |
| Initial annual contribution | £3,000 |
| Annual contribution increase | £100 |
| Inflation | 2% |
| Mean investment return | 5% |
| Investment volatility | 10% |
| Monte Carlo simulations | 10,000 |

These assumptions can be modified at the beginning of the Python script to explore alternative scenarios.

## 1. Deterministic Pension Projection

The first stage calculates the future value of annual pension contributions over the investment horizon.

Contributions increase over time and are adjusted for inflation. Each contribution is then compounded according to the assumed investment return.

The model calculates both:

- **Nominal pension value** – the projected monetary value at retirement.
- **Real pension value** – the projected value adjusted for inflation to make outcomes comparable in today's money.

## 2. Sensitivity Analysis

A two-way sensitivity analysis examines how the real pension value changes when both investment returns and annual contribution increases are varied.

Investment returns are tested between **2% and 6%**, while annual contribution increases range from **£0 to £200**.

The results are displayed using a heatmap, illustrating the long-term impact of changes in investment performance and contribution strategy.

## 3. Monte Carlo Simulation

A deterministic projection assumes the same investment return each year. In reality, investment returns vary over time.

To incorporate this uncertainty, the model performs **10,000 Monte Carlo simulations**.

For each simulation:

1. Annual investment returns are randomly generated using an assumed mean return and volatility.
2. Pension contributions are added each year.
3. The accumulated pension is exposed to the simulated annual investment return.
4. The final pension value is adjusted for inflation.

This produces a distribution of possible real pension outcomes rather than a single estimate.

The model reports summary statistics including:

- Mean pension value
- Median pension value
- 5th percentile
- 95th percentile

A histogram is also generated to visualise the distribution of simulated retirement outcomes.

## 4. Retirement Target Analysis

The simulated pension outcomes are used to estimate the probability of achieving different real pension targets:

- £200,000
- £300,000
- £400,000
- £500,000
- £600,000

This converts the Monte Carlo simulation into a more interpretable measure of retirement risk.

Rather than asking only:

> "What will the pension be worth?"

the model can also investigate:

> "What is the probability of achieving a particular retirement target?"

## 5. Monte Carlo Sensitivity Analysis

The final stage examines how the probability of achieving a **£400,000 real pension target** changes under different investment assumptions.

The model tests combinations of:

**Mean annual return**
- 4%
- 5%
- 6%

**Annual volatility**
- 8%
- 10%
- 12%

For each combination, 10,000 pension outcomes are simulated and the probability of reaching the £400,000 target is calculated.

The resulting heatmap demonstrates how both expected investment performance and investment uncertainty affect the probability of achieving the retirement objective.

## Technologies Used

- Python
- NumPy
- pandas
- Matplotlib

## Running the Model

Install the required packages:

```bash
pip install numpy pandas matplotlib
```

Then run:

```bash
python pension_risk_model.py
```

The model will output the pension projections, Monte Carlo statistics and target probabilities, alongside the sensitivity and distribution visualisations.

## Limitations

This project is intended as an educational actuarial and financial risk modelling exercise rather than a complete pension valuation model.

Key simplifications include:

- Investment returns are modelled using a normal distribution.
- Mean investment return and volatility are assumed to remain constant over time.
- Inflation is assumed to be constant.
- Contributions follow a predetermined pattern.
- Tax, fees, investment charges and pension-specific regulations are not modelled.
- The model does not incorporate mortality or longevity risk.

These assumptions allow the project to focus on the impact of investment uncertainty and long-term compounding.

## Potential Extensions

Possible future developments include:

- Modelling stochastic inflation.
- Introducing different asset allocation strategies.
- Incorporating investment management fees.
- Modelling correlated inflation and investment returns.
- Comparing different contribution strategies.
- Introducing retirement drawdown and longevity risk.

## Purpose

This project was developed to apply probability, simulation and sensitivity analysis to a long-term financial risk problem.

It demonstrates the progression from a deterministic financial model to a stochastic simulation framework, using Python to quantify uncertainty and evaluate the probability of achieving long-term financial targets.
