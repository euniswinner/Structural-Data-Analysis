import pandas as pd
import matplotlib.pyplot as plt

# Hand-collected from FRED 2010-2024
target_years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
hourly_pay = [8.0, 8.0, 8.0, 8.0, 9.0, 9.0, 10.5, 12.0, 13.25, 14.25, 15.0, 15.0, 16.04, 16.78, 17.28]
unemp_val = [12.5, 12.2, 10.9, 8.9, 8.2, 5.9, 5.2, 4.8, 4.6, 4.4, 12.8, 8.9, 4.9, 5.1, 5.4]

# Merge into raw data
raw_data = {'year': target_years, 'wage': hourly_pay, 'unemployment': unemp_val}
la_stats = pd.DataFrame(raw_data)

# Checking year-over-year wage growth
la_stats['wage_diff'] = la_stats['wage'].diff().fillna(0)

# Visualizing the relationship
plt.style.use('bmh')
f, ax_left = plt.subplots(figsize=(10, 5))

# Plotting Wage
ax_left.bar(la_stats['year'], la_stats['wage'], color='darkgrey', label='Min Wage')
ax_left.set_ylabel('Wage (USD)')
ax_left.set_xlabel('Timeline')

# Plotting Unemployment on right axis
ax_right = ax_left.twinx()
ax_right.plot(la_stats['year'], la_stats['unemployment'], color='darkred', marker='D', markersize=5)
ax_right.set_ylabel('Rate (%)')

# Identifying the 2020 Pandemic impact
plt.annotate('2020 COVID Impact', (2020, 12.8), xytext=(2015, 12), arrowprops=dict(facecolor='black', width=1))

plt.title('LA Labor Market: Wage vs Jobless Rate')
plt.show()

# Quick summary for the project
print("--- Correlation Summary ---")
print(la_stats[['wage', 'unemployment']].corr().iloc[0,1])
