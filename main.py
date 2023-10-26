import pandas as pd
from scipy.stats import friedmanchisquare

decision = 3

if decision == 1:
    data_source = "2D"
if decision == 2:
    data_source = "10D"
if decision == 3:
    data_source = "30D"
# Read data from Excel

data = pd.read_excel(f'/Users/milanjanovic/Documents/GitHub/AK9EV_Zapocet/{data_source}_values.xlsx', header=None)

# Convert data rows to lists
algorithms = [data.iloc[i].tolist() for i in range(data.shape[0])]

# Friedman test
chi2, p = friedmanchisquare(*algorithms)  # The asterisk here unpacks all lists into the function.

print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}")

if p < 0.05:
    print("There is a statistically significant difference between the algorithms.")
else:
    print("There is no statistically significant difference between the algorithms.")