import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

np.random.seed(20)

#set assumptions
start_age=21
end_age=66
initial_contrib=3000
increase_per_year=100
inflation=0.02

mean_return=0.05
volatility=0.1
simulations=10000

def pension_value(start_age, end_age, initial_contrib,increase_per_year, interest_rate, inflation):
    years = end_age - start_age
    total_value = 0

    for i in range(1, years + 1):
        contribution = (initial_contrib + (i - 1) * increase_per_year) * (1 + inflation) ** i
        future_value = contribution * (1 + interest_rate) ** (years - i)
        total_value += future_value

    real_value = total_value / (1 + inflation) ** years

    return total_value, real_value

def monte_carlo_simulation(mean_return,volatility,simulations,years,initial_contrib,increase_per_year,inflation):
    results = []

    for simulation in range(simulations):
        returns = np.random.normal(mean_return,volatility,years)

        pension = 0

        for i, return_rate in enumerate(returns, start=1):

            contribution = (initial_contrib +(i - 1) * increase_per_year) * (1 + inflation) ** i
            pension += contribution
            pension *= (1 + return_rate)

        real_pension = pension / (1 + inflation) ** years
        results.append(real_pension)
    return np.array(results)

nominal_pension, real_pension=pension_value(start_age,end_age,initial_contrib,increase_per_year,0.03,inflation)

print(f"Nominal Pension: £{nominal_pension:,.2f}")
print(f"Real Pension: £{real_pension:,.2f}")

#two way sensitive analysis
#How does the final pension change if the investment return changes and annual contribution increases?
rates=[0.02,0.03,0.04,0.05,0.06]
increases=[0,50,100,150,200]
results=[]

for rate in rates:
    for increase in increases:
        nominal, real=pension_value(21,66,3000,increase,rate,0.02)
        results.append({"Return":rate,"Annual increase":increase, "Real Pension":real})

results_df=pd.DataFrame(results)
print(results_df)

heatmap_data = results_df.pivot(index="Return",columns="Annual increase",values="Real Pension")
print(heatmap_data)
plt.imshow(heatmap_data, aspect="auto")
plt.xlabel("Annual contribution increase (£)")
plt.ylabel("Investment return")
plt.title("Real Pension: Two-Way Sensitivity Analysis")
plt.colorbar(label="Real Pension Value (£)")
plt.xticks(range(len(heatmap_data.columns)),heatmap_data.columns)
plt.yticks(range(len(heatmap_data.index)),[f"{x:.0%}" for x in heatmap_data.index])

for i in range(len(heatmap_data.index)):
    for j in range(len(heatmap_data.columns)):
        value = heatmap_data.iloc[i, j]
        plt.text(j, i,f"£{value:,.0f}",ha="center",va="center")
plt.show()

#monte carlo simulation
results=monte_carlo_simulation(mean_return,volatility,simulations,end_age-start_age,initial_contrib,increase_per_year,inflation)
results_df = pd.DataFrame({"Real Pension": results})

print(f"Mean: £{results.mean():,.2f}")
print(f"Median: £{np.median(results):,.2f}")
print(f"5th percentile: £{np.quantile(results, 0.05):,.2f}")
print(f"95th percentile: £{np.quantile(results, 0.95):,.2f}")

#Distribution of simulated pension values
plt.figure()
plt.hist(results_df["Real Pension"])
plt.xlabel("Real Pension (£)")
plt.ylabel("Number of Simulations")
plt.title("Distribution of Simulated Real Pension Values")
plt.show()

targets = [200000, 300000, 400000, 500000, 600000]

probabilities=[]
for target in targets:
    probability=(results_df["Real Pension"]>=target).mean()*100
    probabilities.append({"Target Pension":target,"Probability":probability})
probability_df=pd.DataFrame(probabilities)
    
print(probability_df)

returns = np.random.normal(mean_return, volatility, 10000)

print("Mean:", returns.mean())
print("Minimum:", returns.min())
print("Maximum:", returns.max())

mean_returns = [0.04, 0.05, 0.06]
volatilities = [0.08, 0.10, 0.12]
target = 400000

mc_sensitivity_results = []

for mean_return in mean_returns:
    for volatility in volatilities:
        results = monte_carlo_simulation(mean_return,volatility,simulations,end_age-start_age,initial_contrib,increase_per_year,inflation)
        probability = (results >= target).mean() * 100
        mc_sensitivity_results.append({"Mean Return": mean_return,"Volatility": volatility,"Probability": probability})   
mc_sensitivity_df = pd.DataFrame(mc_sensitivity_results)
print(mc_sensitivity_df)

mc_heatmap = mc_sensitivity_df.pivot(index="Mean Return",columns="Volatility",values="Probability")

plt.figure()
plt.imshow(mc_heatmap, aspect="auto")
plt.xlabel("Investment Volatility")
plt.ylabel("Mean Investment Return")
plt.title("Probability of Achieving £400,000 Real Pension")
plt.colorbar(label="Probability (%)")
plt.xticks(range(len(mc_heatmap.columns)),[f"{x:.0%}" for x in mc_heatmap.columns])
plt.yticks(range(len(mc_heatmap.index)),[f"{x:.0%}" for x in mc_heatmap.index])

for i in range(len(mc_heatmap.index)):
    for j in range(len(mc_heatmap.columns)):
        value = mc_heatmap.iloc[i, j]
        plt.text(j, i, f"{value:.1f}%",ha="center", va="center")

plt.show()




