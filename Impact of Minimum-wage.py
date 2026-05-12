import pandas as pd
import matplotlib.pyplot as plt

# Load LA economic dataset (compiled from FRED/BLS)
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
min_wages = [8.0, 8.0, 8.0, 8.0, 9.0, 9.0, 10.5, 12.0, 13.25, 14.25, 15.0, 15.0, 16.04, 16.78, 17.28]
unemp_rates = [12.5, 12.2, 10.9, 8.9, 8.2, 5.9, 5.2, 4.8, 4.6, 4.4, 12.8, 8.9, 4.9, 5.1, 5.4]

# Create processing dataframe
la_econ_df = pd.DataFrame({
    'time_period': years,
    'hourly_wage': min_wages,
    'unemp_rate': unemp_rates
})

# Setup visualization
plt.figure(figsize=(11, 5))
fig, main_ax = plt.subplots()

# Primary: Min Wage Trend
main_ax.bar(la_econ_df['time_period'], la_econ_df['hourly_wage'], color='#95a5a6', alpha=0.4, label='Min Wage')
main_ax.set_ylabel('Wage in USD')

# Secondary: Job Market Impact
trend_ax = main_ax.twinx()
trend_ax.plot(la_econ_df['time_period'], la_econ_df['unemp_rate'], color='#c0392b', marker='s', markersize=4, label='Unemployment %')
trend_ax.set_ylabel('Unemployment Rate (%)')

# Note: Outlier due to Pandemic
plt.title('Analysis of LA Minimum Wage vs Unemployment')
plt.annotate('COVID Outlier', xy=(2020, 12.8), xytext=(2016, 13), 
             arrowprops=dict(arrowstyle='->', lw=1, color='black'))

plt.tight_layout()
plt.show()

# Final Correlation Check
print("Correlation result:")
print(la_econ_df[['hourly_wage', 'unemp_rate']].corr())
